import re
from tqdm import tqdm
from pathlib import Path
from src.service.generator.llm_response import llm_response
from src.service.document.load_document import load_json, save_json, parse_path_info, updata_document_metadata

def generate_equation_description(
    equation: str,
    relative_sentence: str,
    temperature: float = 0.5
) -> dict:
    """
    Generate an equation–description pair using contextual sentences.

    Args:
        equation (str): The equation to be described, e.g. "$y = x^2$".
        relative_sentence (str): Sentences in the paper related to the equation.
        temperature (float): LLM temperature. Defaults to 0.5.

    Returns:
        dict: {
            "equation": str,
            "description": str
        }
    """

    system_prompt = (
        "You are an expert in academic paper structure and scientific scientific writing.\n"
        "Your task is to produce a formal, journal-style description of a given equation.\n\n"
        f"Equation:\n{equation}\n\n"
        "Relevant context from the manuscript:\n"
        f"{relative_sentence}\n\n"
        "Write a concise explanatory paragraph that *describes* the equation rather than "
        "rewriting or transforming it. Use standard scientific prose, introducing variables "
        "with phrases such as 'where', 'denotes', or 'represents'. Clearly define all symbols "
        "appearing in the equation and briefly explain the physical or mathematical relationship "
        "captured by the equation.\n\n"
        "Do not modify, rearrange, or restate the equation itself. "
        "If the meaning or role of the equation cannot be inferred from the equation and the "
        "provided context, return exactly: 'Not clear'"
    )

    response = llm_response(
        query=equation,
        system_prompt=system_prompt,
        temperature=temperature
    ).strip()

    if response.lower() == "not clear" or  response.lower() == "not clear." or len(response.strip().split()) < 5:
        return None

    return {
        "equation": equation,
        "description": response
    }
    
def identify_equation(
    file_data: dict,
    temperature: float = 0.8,
    reidentify: bool = False
) -> dict:
    """
    Identify equations and generate equation–description pairs.

    Args:
        file_data (dict): Metadata dictionary containing:
            - file_name
            - file_type
            - file_path
            - file_id
            - file_size
            - update_time
            - parsing_status
            - batch_id (optional)
            - DOI_state (optional)
            - doi (optional)
            - clean_state (optional)
            - equation_state (optional)

        temperature (float): LLM temperature. Defaults to 0.8.

    Returns:
        dict: The updated file data with equation–description pairs.
    """
    if reidentify == False:
        if "equation_state" not in file_data:
            file_data["equation_state"] = "None"

        elif file_data["equation_state"] == "done" or file_data["equation_state"] == "Not_Found":
            return file_data

    username, dataset_name = parse_path_info(file_data["file_path"])

    label_path = Path(
        f"users/{username}/{dataset_name}/data_clean/"
        f"{file_data['file_id']}/label_structure_cleaned.json"
    )
    equation_path = Path(
        f"users/{username}/{dataset_name}/data_clean/"
        f"{file_data['file_id']}/equation.json"
    )

    label_structure = load_json(label_path)
    equation_pairs = []

    # ---------- helpers ----------
    def split_sentences(text: str):
        """Sentence split based on punctuation."""
        return [
            s.strip()
            for s in re.split(r"(?<=[.!?])\s+", text)
            if s.strip()
        ]

    def extract_equations(sentence: str):
        """
        Extract inline or display equations from a sentence.
        Returns equations WITH delimiters.
        """
        equations = []

        # display math
        for m in re.findall(r"\$\$(.+?)\$\$", sentence):
            equations.append(f"$${m}$$")

        # inline math
        for m in re.findall(r"\$(.+?)\$", sentence):
            equations.append(f"${m}$")

        return equations

    # ---------- locate main_letter chunks ----------
    main_letter_id = [
        i for i, chunk in enumerate(label_structure)
        if chunk.get("category") == "main_letter"
    ]

    main_letter_index = -1

    with tqdm(
        total=len(label_structure),
        desc=f"Identifying equation [{file_data['file_name'][:5]}..]",
        unit="chunk",
        ncols=100,
        position=0,
        leave=False,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} "
                "[{elapsed}<{remaining}, {rate_fmt}]"
    ) as pbar:
        # ---------- main scan ----------
        for i, chunk in enumerate(label_structure):

            category = chunk.get("category")
            if category not in {"main_letter", "equation"}:
                continue

            if category == "main_letter":
                main_letter_index += 1

            # ==================================================
            # 1. Standalone equation chunk
            # ==================================================
            if category == "equation":
                context_sentences = []

                equation = chunk.get("content", "").strip()
                if not equation:
                    continue
                # previous main_letter
                if main_letter_index >= 0:
                    prev_chunk = label_structure[main_letter_id[main_letter_index]]
                    prev_sents = split_sentences(prev_chunk.get("content", ""))
                    context_sentences.extend(prev_sents[-2:])

                # equation itself
                context_sentences.append(equation)

                # next main_letter
                if main_letter_index + 1 < len(main_letter_id):
                    next_chunk = label_structure[main_letter_id[main_letter_index + 1]]
                    next_sents = split_sentences(next_chunk.get("content", ""))
                    context_sentences.extend(next_sents[:2])

                equation_pairs.append(                
                    generate_equation_description(
                        equation=equation,
                        relative_sentence=" ".join(context_sentences),
                        temperature=temperature
                    ))

            # ==================================================
            # 2. Main_letter chunk
            # ==================================================
            content = chunk.get("content", "")
            if "$" not in content:
                continue

            sentences = split_sentences(content)

            for j, sent in enumerate(sentences):

                if "$" not in sent:
                    continue

                equations = extract_equations(sent)
                if not equations:
                    continue

                for equation in equations:
                    if '=' not in equation or len(equation) < 10: 
                        continue

                    context_sentences = []

                    # ---- previous chunk boundary ----
                    if j == 0 and main_letter_index > 0:
                        prev_chunk = label_structure[
                            main_letter_id[main_letter_index - 1]
                        ]
                        prev_sents = split_sentences(prev_chunk.get("content", ""))
                        context_sentences.extend(prev_sents[-2:])

                    # ---- previous sentences ----
                    context_sentences.extend(sentences[max(0, j - 2):j])

                    # ---- current sentence ----
                    context_sentences.append(sent)

                    # ---- next sentences ----
                    context_sentences.extend(sentences[j + 1:j + 3])

                    # ---- next chunk boundary ----
                    if j == len(sentences) - 1 and main_letter_index + 1 < len(main_letter_id):
                        next_chunk = label_structure[
                            main_letter_id[main_letter_index + 1]
                        ]
                        next_sents = split_sentences(next_chunk.get("content", ""))
                        context_sentences.extend(next_sents[:2])

                    response = generate_equation_description(
                        equation=equation,
                        relative_sentence=" ".join(context_sentences),
                        temperature=temperature
                    )

                    if response:
                        equation_pairs.append(response)
            pbar.update(1)

    # ---------- save ----------
    if equation_pairs:
        file_data["equation_state"] = 'done' 
        updata_document_metadata(username, dataset_name, file_data, info=False)
        save_json(equation_pairs, equation_path) 
    else:
        file_data["equation_state"] = 'Not_Found'
        updata_document_metadata(username, dataset_name, file_data, info=False) 
    return file_data
