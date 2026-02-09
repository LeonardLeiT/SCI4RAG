import os
import re
from tqdm import tqdm
from pathlib import Path
from src.service.generator.llm_response import llm_response
from src.service.document.load_document import load_json, save_json, parse_path_info, updata_document_metadata

def load_markdown(file_data: dict) -> str:
    """
    Load a parsed markdown (.md) file and return its content as a string.

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

    Returns:
        str: Content of the markdown file.
    """

    username, dataset_name = parse_path_info(file_data["file_path"])  
    # MinerU default output path
    md_path = os.path.join(
        "users",
        username,
        dataset_name,
        "parse",
        file_data["file_id"],
        "full.md"
    )
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    if not md_path.lower().endswith(".md"):
        raise ValueError(f"Not a markdown file: {md_path}")

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    return content
    
def chunk_markdown_by_blank_lines(md_text: str) -> list[str]:
    """
    Chunk markdown content by blank lines (lines without any words).

    Args:
        md_text (str): The markdown content as a string.

    Returns:
        list[str]: List of markdown chunks.
    """
    chunks = []
    buffer = []

    for line in md_text.splitlines():
        # Line without any words (blank or whitespace)
        if line.strip() == "":
            if buffer:
                chunks.append("\n".join(buffer).strip())
                buffer = []
        else:
            buffer.append(line)

    # Add last chunk
    if buffer:
        chunks.append("\n".join(buffer).strip())

    return chunks
def chunk_identify_main_section(
    query: str,
    CATEGORIES = {
        "title",
        "abstract",
        "keywords",
        "main_letter",
        "references",
        "other",
    },
    temperature: float = 0.1
    ) -> str:
    """ Identify main structure which academic paper section the input text belongs to. 
    Title, Abstract, Keywords, Main Letter, References, Other, figure_url, table. 
    Parameters: 
        query : str Current text chunk to classify. 
        CATEGORIES : set Predefined main section labels. 
    Returns: 
        str The identified section category. 
    """

    # --- build system prompt dynamically ---
    system_prompt = "You are an expert in academic paper structure analysis.\n"
    system_prompt += "Classify the given text into ONE of the following categories ONLY:\n\n"
    system_prompt += f"{', '.join(CATEGORIES)}\n\n"
    system_prompt += "Category definitions:\n"

    if "title" in CATEGORIES:
        system_prompt += (
            "title: The main title of the paper, must more than 4 words long."
            "Examples: # Enhanced thermal stability of nanograined metals below a critical grain size' \n\n"
        )
    if "abstract" in CATEGORIES:
        system_prompt += "abstract: The abstract of the paper, a brief summary of its main findings.\n\n"
    if "keywords" in CATEGORIES:
        system_prompt += (
            "keywords: A list of important terms or phrases summarizing the main topics of the paper. It must be scientifically relevant.\n\n"
            "Example: 'nanomaterials, thermal stability, grain size, molecular dynamics simulations, Hall-petch relationship.'\n\n"
        )
    if "main_letter" in CATEGORIES:
        system_prompt += (
            "main_letter: The main body of the paper containing the introduction, methods, results, and discussion. "
            "This category does NOT include author-related sections such as Author Information or Author Contributions, NOT article info such financially supported.\n\n" 
        )
    if "references" in CATEGORIES:
        system_prompt += (
            "references: Bibliographic entries containing author names, article title, journal name, year, volume, and pages. "
            "Example: 'Andrievski, R. Review of thermal stability of nanomaterials. J. Mater. Sci. 2014, 49, 1449-1460.'\n\n"
        )
    if "figure_url" in CATEGORIES:
        system_prompt += "figure_url: Links to figures (e.g., `![Figure](url)`).\n\n"
    if "table" in CATEGORIES:
        system_prompt += "table: Table contents, usually in Markdown table format (`| ... |`).\n\n"
    if "other" in CATEGORIES:
        system_prompt += "other: Noise or non-paper-body content, such as author-related sections (Author Information, Author Contributions), financial support, or any text that does not fit into the above categories. And Journal name, publication information, or identifiers such as DOI, or URL. Also the Names of the authors\n\n"
    system_prompt += (       
        "Rules:\n"
        "1. Return ONLY the category name.\n"
        "2. Do NOT add explanations or extra text.\n"
        "3. If uncertain, return 'other'.\n"
    )
    # print(system_prompt)
    # --- call LLM ---
    response = llm_response(query=query, system_prompt=system_prompt, temperature=temperature).strip().lower()
    # print(f"Category: {response}")
    # --- safety guard ---
    if response not in CATEGORIES:
        response = "other"

    if response == "title":
        if len(query.split()) < 4:
            response = "other"

    if response == "abstract":
        if len(query.split()) < 10:
            response = "other"

    if response == "references":
        if len(query) < 10:
            response = "other"

    return response


# 1. First identify main section-> clean_state = "identified_main_section"
def identify_main_section(file_data: dict, reidentify = False) -> str:
    """ 
    Identify main structure which academic paper section the markdown chunks belongs to.
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

    Returns: 
        file_data (dict): Updated file_data with clean_state.
    """

    # ---- clean_state guard ----
    if file_data["DOI_state"] != "Doi_Updated":
        print(f"{file_data['file_name']}: Need to update DOI first") 
        return file_data

    # ---- load markdown ----
    content_markdown = load_markdown(file_data)
    chunks = chunk_markdown_by_blank_lines(content_markdown)

    username, dataset_name = parse_path_info(file_data["file_path"])
    label_path = Path(
    f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/label_structure.json"
    )
    label_path.parent.mkdir(parents=True, exist_ok=True)

    if reidentify == False:
        if "clean_state" not in file_data: 
            file_data["clean_state"] = "Not_Cleaned"
        else: 
            if file_data["clean_state"] in {
                "identified_main_section",
                "identified",
                "Cleaned"
            }:
                print(f"{file_data['file_name']}: Already {file_data['clean_state']}") 
                return file_data
            
        if file_data["clean_state"] == "Not_Standard_Letter":
            print(f"{file_data['file_name']}: Not Standard Letter")
            return file_data

    # ---- load existing labels if exist ----
    if label_path.exists(): 
        structured_chunks = load_json(label_path)
    else: 
        structured_chunks = []
    structured_chunks = []

   # ---- initial categories ----     
    BASE_CATEGORIES = {
        "title",
        "other",
    }
    CATEGORIES = set(BASE_CATEGORIES)

    with tqdm(
        total=len(chunks),
        desc=f"Identifying sections [{file_data['file_name'][:5]}..]",
        unit="chunk",
        ncols=100,
        position=0,
        leave=False,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} "
                "[{elapsed}<{remaining}, {rate_fmt}]"
    ) as pbar:
        for i, chunk in enumerate(chunks):
            # ---- reuse existing label if present ----
            if i < len(structured_chunks):
                label = structured_chunks[i]["category"]
            else:
                label = chunk_identify_main_section(query=chunk, CATEGORIES=CATEGORIES)
                structured_chunks.append({
                    "id": i,
                    "category": label,
                    "content": chunk
                })
                
                #--  save progress every 10 chunks ---
                if i % 30 == 0:
                    file_data["clean_state"] = "identifying_in_progress"
                    updata_document_metadata(username, dataset_name, file_data, info=False)
                    save_json(structured_chunks, label_path, info=False)

            # ---- state logic ----
            if label == "title":
                CATEGORIES.discard("title")
                CATEGORIES.add("abstract")
                CATEGORIES.add("keywords")
            if label == "abstract":
                CATEGORIES.discard("abstract")
                CATEGORIES.add("main_letter")
                CATEGORIES.add("references")
                CATEGORIES.add("figure_url")
                CATEGORIES.add("table")
            elif label == "main_letter":
                CATEGORIES.discard("other")
            elif label == "references":
                CATEGORIES.discard("figure_url")
                CATEGORIES.discard("table")
                CATEGORIES.discard("main_letter")
                CATEGORIES.add("other")
            pbar.update(1)
    save_json(structured_chunks, label_path)
    
    if "main_letter" in CATEGORIES:
        file_data["clean_state"] = "identified_main_section"
    else:
        file_data["clean_state"] = "Not_Standard_Letter"
    updata_document_metadata(username, dataset_name, file_data, info=False)
    return file_data

# 2. Second identify mian letter detail section-> clean_state = "identified"
def identify_detail(file_data: dict, reidentify = False) -> str:
    """ Identify equation, figure and thoses discribetion which academic paper section the markdown chunks belongs to, using rules and LLM.
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

    Returns: 
        file_data (dict): Updated file_data with clean_state.
    """

    # ---- clean_state guard ----
    if file_data["DOI_state"] != "Doi_Updated":
        print(f"{file_data['file_name']}: Need to update DOI first") 
        return file_data
    
    if reidentify == False:
        if "clean_state" not in file_data: 
            file_data["clean_state"] = "Not_Cleaned"
        else: 
            if file_data["clean_state"] in {
                "identified",
                "Cleaned" 
            }:
                print(f"{file_data['file_name']}: Already {file_data['clean_state']}") 
                return file_data
        
    # ---- load markdown ----
    username, dataset_name = parse_path_info(file_data["file_path"])
    label_path = Path(
    f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/label_structure.json"
    )

    label_structure = load_json(label_path)
    new_label_structure = []

    # ---- find the range of interest ----
    start_id = None
    end_id = None
    ref_id = None
    for idx, chunk_json in enumerate(label_structure):
        cat = chunk_json.get("category", "").lower()
        if cat == "abstract" and start_id is None:
            start_id = idx
        if cat == "main_letter":
            end_id = idx  
        if cat == "references" and ref_id is None:
            ref_id = idx

    if ref_id < end_id: 
        end_id = ref_id

    for idx, chunk_json in enumerate(label_structure):
        if start_id < idx < end_id:
            content = chunk_json.get("content", "").strip()
            # equation
            if content.startswith("$$") and content.endswith("$$"):
                chunk_json["category"] = "equation"
            # figure markdown
            elif "images/" in content and "![](images/" in content:
                chunk_json['category'] = "figure_url"
            # section titles (optional)

            if content == "# R E P O R T S":
                chunk_json["category"] = "other"

            if chunk_json["category"] == "other":
                if content.startswith("#"):
                    text = content.lstrip("#").strip()
                    is_numbered = bool(re.match(r"^\d+(\.\d+)*\b", text))
                    if is_numbered:
                        chunk_json["category"] = "main_letter"
                    if '.' not in content and ']' in content:
                        chunk_json["category"] = "main_letter"
        new_label_structure.append(chunk_json)    

    # label_path = Path(
    # f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/label_structure1.json"
    # )    
    save_json(new_label_structure, label_path)
    file_data["clean_state"] = "identified"
    updata_document_metadata(username, dataset_name, file_data)
    return file_data

# 3. Third combine label structure and delete other info -> clean_state = "cleaned"
def combine_label_structure(file_data: dict) -> dict:
    """
    Combine label_structure chunks with rules:
    - keywords: merge all into one id with list
    - main_letter: punctuation-aware sentence merging (.;?!)
      - sentence can continue across figure/table blocks
    - reference: merge all into ONE json, separated by '\\n'
    - figure / table / *_url: keep original json

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

    Returns: 
        file_data (dict): Updated file_data with clean_state.
    """
    if file_data["DOI_state"] != "Doi_Updated":
        print(f"{file_data['file_name']}: Need to update DOI first") 
        return file_data

    if "clean_state" not in file_data: 
        file_data["clean_state"] = "Not_Cleaned"
    else: 
        if file_data["clean_state"] in {
            "Cleaned" 
        }:
            print(f"{file_data['file_name']}: Already {file_data['clean_state']}") 
            return file_data
        
    username, dataset_name = parse_path_info(file_data["file_path"])

    label_path = Path(
        f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/label_structure.json"
    )
    label_structure = load_json(label_path)

    new_label_structure = []

    main_buffer = ""
    main_active = False

    reference_buffer = ""

    figure_buffer = ""
    figure_active = False

    jdx = 0

    STOP_PUNCT = (".", ";", "?", "!", ":")

    NON_TEXT = {"table"}

    def is_sentence_end(text: str) -> bool:
        return text.rstrip().endswith(STOP_PUNCT)
    
    HEADER_BLOCK_SIGNS = set("}])!~\\/")

    def is_pure_header(text: str) -> bool:
        """
        A pure section header:
        - starts with '#'
        - contains no other structural signs
        """
        if not text.startswith("#"):
            return False
        return not any(ch in HEADER_BLOCK_SIGNS for ch in text)

    def flush_main():
        nonlocal jdx, main_buffer, main_active
        if main_active and main_buffer.strip():
            new_label_structure.append({
                "id": jdx,
                "category": "main_letter",
                "content": main_buffer.strip()
            })
            jdx += 1
        main_buffer = ""
        main_active = False

    def flush_figure():
        nonlocal jdx, figure_buffer, figure_active
        if figure_active and figure_buffer.strip():
            new_label_structure.append({
                "id": jdx,
                "category": "figure_url",
                "content": figure_buffer.strip()
            })
            jdx += 1
        figure_buffer = ""
        figure_active = False

    for chunk in label_structure:
        category = chunk.get("category")
        content = chunk.get("content", "")
        if isinstance(content, list):
            # If it's a list, join it into a string
            content = " ".join(str(c) for c in content)
        elif content is None:
            content = ""
        content = content.strip()

        # 1.skip others
        if category in {"other", "title", "keywords"}:
            continue

        # 3.references
        if category == "references":
            if reference_buffer:
                reference_buffer += " " + content
            else:
                reference_buffer = content

            if is_sentence_end(content):
                reference_buffer += "\n"
            continue

        # 4.figure_url
        if category == "figure_url":
            if figure_active:
                figure_buffer += "\n" + content
            else:
                figure_active = True
                figure_buffer = content
            continue
        flush_figure()

        # 4. non-text blocks
        if category in NON_TEXT:
            new_label_structure.append({
                "id": jdx,
                "category": category,
                "content": content
            })
            jdx += 1
            continue

        # 5. main_letter
        if category == "main_letter":
            if is_pure_header(content):
                flush_main()
                new_label_structure.append({
                    "id": jdx,
                    "category": "main_letter",
                    "content": content
                })
                jdx += 1
                continue

            if not main_active:
                main_active = True
                main_buffer = content
            else:
                main_buffer += " " + content

            if is_sentence_end(content):
                flush_main()
            continue
        flush_main()

        if category in "equation":
            new_label_structure.append({
                "id": jdx,
                "category": category,
                "content": content
            })
            jdx += 1
            continue

        new_label_structure.append({
            "id": jdx,
            "category": category,
            "content": content
        })
        jdx += 1

    flush_main()

    # ---------- insert reference ----------
    if reference_buffer.strip():
        new_label_structure.append({
            "id": jdx,
            "category": "reference",
            "content": reference_buffer.rstrip()
        })

    new_label_path = Path(
        f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/label_structure_cleaned.json")
    
    # file_data["clean_state"] = True
    save_json(new_label_structure, new_label_path)
    file_data["clean_state"] = "Cleaned"
    updata_document_metadata(username, dataset_name, file_data)
    return file_data

def combile_doc_json(file_data: dict) -> str:
    """ Combile markdown chunks into one markdown file.
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

    Returns: 
        file_data (dict): Updated file_data with clean_state.
    """
    username, dataset_name = parse_path_info(file_data["file_path"])
    base = Path("users") / username / dataset_name / "data_clean" / file_data["file_id"]

    doc_json_path = base / "main_letter.json"
    label_path = base / "label_structure_cleaned.json"
    doi_path = base / "doi.json"

    if not label_path.exists() or not doi_path.exists():
        print(f"[WARN] Missing clean files for {file_data['file_id']}")
        return file_data

    label_info = load_json(label_path)
    doi_info = load_json(doi_path)

    doc_json = {
        "title": doi_info.get("title", ""),
        "author": doi_info.get("author", ""),
        "journal": doi_info.get("journal", ""),
        "doi": doi_info.get("doi", ""),
        "abstract": "",
        "keywords": [],
        "main_letter": {},
    }

    jdx = 0
    for idx, chunk in enumerate(label_info):
        category = chunk.get("category")
        content = chunk.get("content", "")

        if not content:
            continue

        if category == "abstract":
            doc_json["abstract"] = content

        elif category == "main_letter" or category == "equation":
            doc_json["main_letter"][jdx] = content
            jdx += 1

    save_json(doc_json, doc_json_path)

    return file_data