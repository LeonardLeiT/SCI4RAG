import re
from pathlib import Path
from src.service.generator.llm_response import llm_response
from src.service.document.load_document import load_json, save_json, parse_path_info, updata_document_metadata

def check_keywords(
        content: str, 
        title: str, 
        abstract: str,
        temperature: float = 0.8
    )-> bool:
    """
    Check whether the keywords in the file are consistent with the title and abstract.

    Args:
        content (str): The content of the file.
        title (str): The title of the file.
        abstract (str): The abstract of the file.
        temperature (float, optional): The temperature of the LLM. Defaults to 0.8.

    Returns:
        bool: Whether the keywords in the file are consistent with the title and abstract.

    Raises:
        ValueError: If the keywords are not consistent with the title and abstract.
    """
    system_prompt = (
        "You are an expert in analyzing whether content represents valid keywords in a parsed article PDF.\n"
        "Your task is to check whether the provided content constitutes valid paper keywords according to the given title and abstract.\n\n"
        "Keywords should describe core topics, methods (experiment, simulation), materials, elements, or phenomena.\n\n"
        f"Title: {title}\n"
        f"Abstract: {abstract}\n"
        "Return ONLY one word: True or False."
    )

    response = llm_response(
        query=content,
        system_prompt=system_prompt,
        temperature=temperature
    ).strip().lower()

    if  response == "true":
        return True
    else:
        return False   

# sreach keywords in parse file
def search_keywords(file_data: dict) -> dict:
    """
    search keywords in parse file if there are keywords in the file, return the keywords and the sentences containing the keywords.

    Args:
        file_data (dict): The metadata of the file.

    Returns:
        dict: The processed file data.
    """
    username, dataset_name = parse_path_info(file_data["file_path"])

    label_path = Path(
        f"users/{username}/{dataset_name}/data_clean/"
        f"{file_data['file_id']}/label_structure.json"
    )
    doi_path = Path(
        f"users/{username}/{dataset_name}/data_clean/"
        f"{file_data['file_id']}/doi.json"
    )

    label_structure = load_json(label_path)
    doi_info = load_json(doi_path)
    title = doi_info.get("title")
    abstract = doi_info.get("abstract")

    keyword_exist = False
    keywords = ''
    for chunk in label_structure:
        if chunk.get("category") == "keywords":
            if keyword_exist == False:
                idx_keyword = chunk.get("id")
                keyword_exist = True
                keywords = chunk.get("content")
            else:
                keywords += ", " + chunk.get("content")

    if keyword_exist:
        for chunk in label_structure:
            if chunk.get("id") > idx_keyword:
                if chunk.get("category") == "main_letter":
                    break
                if chunk.get("category") == "keywords":
                    continue
                if chunk.get("category") == "abstract":
                    continue                    
                content = chunk.get("content")
                if len(content.strip().split()) < 4:
                    check_state = check_keywords(content, title, abstract)
                    if check_state == True:
                        keywords += ", " + chunk.get("content")
    return keywords

def extract_keywords(keyword_text: str):
    """
    Extract keyword list from a keyword string.
    Removes 'keywords' labels and splits by comma.
    """
    # remove leading labels like "KEYWORDS:" or "# Keywords:"
    cleaned = re.sub(r"^\s*#?\s*keywords\s*:\s*", "", keyword_text, flags=re.IGNORECASE)

    # split by comma and strip whitespace
    keywords = [k.strip() for k in cleaned.split(",") if k.strip()]

    return keywords

def identify_keywords(file_data: dict) -> dict:
    """
    Identify the keywords in the file.

    Args:
        file_data (dict): The metadata of the file.

    Returns:
        dict: The processed file data.
    """
    username, dataset_name = parse_path_info(file_data["file_path"])

    doi_path = Path(
        f"users/{username}/{dataset_name}/data_clean/"
        f"{file_data['file_id']}/doi.json"
    )

    label_path = Path(
        f"users/{username}/{dataset_name}/data_clean)/"
        f"{file_data['file_id']}/label_structure.json"
    )

    letter_path = Path(
        f"users/{username}/{dataset_name}/data_clean/"
        f"{file_data['file_id']}/main_letter.json"
    )

    doi_info = load_json(doi_path)
    label_structure = load_json(label_path)
    main_letter = load_json(letter_path)

    # search keywords in parse file
    keywords = extract_keywords(search_keywords(file_data))
    if keywords:
        doi_info['keywords'] = keywords
        main_letter['keywords'] = keywords
        save_json(doi_info, doi_path)
        save_json(main_letter, letter_path)

