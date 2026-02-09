import re
from typing import List, Dict
from tqdm import tqdm
from pathlib import Path
from src.service.agent.article_information import get_reference_info
from src.service.document.load_document import load_json, save_json, parse_path_info, updata_document_metadata
def split_references(reference_text: str, characters: int = 20) -> List[Dict]:
    """
    Split a reference block into individual references.
    Supports numbering styles:
        [1] ... , (1) ... , 1. ...

    Only keeps references with at least `min_words` words.

    Args:
        reference_text (str): Raw reference text.
        min_words (int): Minimum words to keep a reference.

    Returns:
        List[Dict]: [{"ref_id": int, "content": str}, ...]
    """
    if not reference_text:
        return []

    reference_text = reference_text.strip()
    # Remove headers like "# REFERENCES" or "REFERENCES"
    reference_text = re.sub(r'^\s*#?\s*references?\s*', '', reference_text, flags=re.IGNORECASE)

    # Determine numbering style
    style = None
    if re.search(r'^\[\d+\]', reference_text):
        style = 'bracket'
        split_pattern = r'(?=\[\d+\])'
        id_pattern = r'\[(\d+)\]\s*(.*)'
    elif re.search(r'^\(\d+\)', reference_text):
        style = 'paren'
        split_pattern = r'(?=\(\d+\))'
        id_pattern = r'\((\d+)\)\s*(.*)'
    elif re.search(r'^\d+\.', reference_text):
        style = 'dot'
        split_pattern = r'(?=\d+\.)'
        id_pattern = r'(\d+)\.\s*(.*)'
    else:
        # Unknown format
        return []

    parts = re.split(split_pattern, reference_text)
    references = []

    for part in parts:
        part = part.strip()
        if not part:
            continue

        match = re.match(id_pattern, part, re.DOTALL)
        if not match:
            continue

        ref_id, content = match.groups()
        content_clean = content.strip()

        # Only keep if number of words > min_words
        if len(content_clean) >= characters:
            references.append(content_clean)

    return references

def process_references(file_data: dict, reidentify = False) -> List[Dict]:
    """
    Process references for a given file.

    Args:
        file_data (dict): The metadata of the file.

    Returns:
        List[Dict]: The processed references.
    """
    if reidentify == False:
        if "reference_state" not in file_data:
            file_data['reference_state']='None'

        elif file_data["reference_state"] == "done" or file_data["reference_state"] == "Not_Found":
            return file_data

    username, dataset_name = parse_path_info(file_data["file_path"])

    label_path = Path(
        f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/label_structure_cleaned.json"
    )

    references_path = Path(
        f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/references.json"
    )

    label_structure = load_json(label_path)
    raw_references: List[str] = []

    # Extract raw reference strings
    for chunk in label_structure:
        if chunk.get("category") == "reference":
            content = chunk.get("content", "")
            if content.strip():
                raw_references.extend(split_references(content))

    processed_references: Dict[str, Dict] = {}
    with tqdm(
        total=len(raw_references),
        desc=f"agent ref_info [{file_data['file_name'][:8]}..]",
        unit="ref",
        ncols=100,
        position=0,
        leave=False,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"
    ) as pbar:
        for ref in raw_references:
            ref_info = get_reference_info(ref)
            # doi = ref_info.get("doi", ref)  # fallback to raw ref if DOI missing
            processed_references[ref] = ref_info
            pbar.update(1)

    if processed_references:
        file_data["reference_state"] = 'done' 
        updata_document_metadata(username, dataset_name, file_data, info=False)
        save_json(processed_references, references_path)
    else:
        file_data["reference_state"] = 'Not_Found'
        updata_document_metadata(username, dataset_name, file_data, info=False)
    return file_data