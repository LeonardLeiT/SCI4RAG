import re
import time
import shutil
import requests
from pathlib import Path
from src.service.document.load_document import load_json, save_json, parse_path_info, updata_document_metadata, load_document_metadata, delete_file

DOI_PATTERN = re.compile(
    r'(?:doi\s*[:：]?\s*|https?://doi\.org/)'  # DOI prefix
    # r'.*?'                                     # any chars, non-greedy
    r'(10\.\d{4,9}/[^\s\]\)]+)',              # DOI number
    re.IGNORECASE
)
def find_first_doi(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            doi = find_first_doi(v)
            if doi:
                return doi
    elif isinstance(obj, list):
        for item in obj:
            doi = find_first_doi(item)
            if doi:
                return doi
    elif isinstance(obj, str):
        match = DOI_PATTERN.search(obj)
        if match:
            return match.group(1)
    return None

def identify_DOI(file_data: dict) -> str:
    """ Identify main structure which academic paper section the markdown chunks belongs to.
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
        file_data (dict): Updated file_data with DOI_state.
    """

    # ---- DOI_state guard ----
    if "DOI_state" not in file_data:
        file_data["DOI_state"] = "Not_DOI"
    else:
        if file_data["DOI_state"] in {
            "Doi_Getted",
            "Doi_Info_Getted",
            "Doi_Updated"
        }:
            print(f"{file_data['file_name']}: Already {file_data['DOI_state']}, skip DOI identification")
            return file_data

    # ---- paths ----
    username, dataset_name = parse_path_info(file_data["file_path"])

    # ---- load layout.json ----
    parse_layout_path = Path(
        f"users/{username}/{dataset_name}/parse/{file_data['file_id']}/layout.json"
    )
    parse_layout = load_json(parse_layout_path)

    doi = find_first_doi(parse_layout)

    # ---- save ----
    file_data["doi"] = doi
    if doi:  # if doi is not None
        file_data["DOI_state"] = "Doi_Getted"
        updata_document_metadata(username, dataset_name, file_data)
    elif doi in (None, "", "null", "Null", "NULL"):
        file_data["DOI_state"] = "Not_DOI"
        updata_document_metadata(username, dataset_name, file_data)
        print(f"{file_data['file_name']}: DOI not found")
    else:
        file_data["DOI_state"] = "Not_DOI"
        updata_document_metadata(username, dataset_name, file_data)
        print(f"{file_data['file_name']}: DOI not found")
    return file_data

def query_crossref(reference: str):
    """
    Use Crossref to search metadata using a reference string.
    Returns metadata dict or None if not found.
    """
    url = "https://api.crossref.org/works"
    params = {
        "query.bibliographic": reference,  # reference string
        "rows": 1                          # return top 1 match
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            items = response.json().get("message", {}).get("items", [])
            if items:
                return items[0]  # metadata dictionary
    except Exception as e:
        print("Error querying Crossref:", e)
    return None

def fetch_article_info_by_doi(doi: str) -> dict:
    """
    Fetch article metadata from Crossref using DOI.

    Args:
        doi (str): The DOI of the article.

    Returns:
        dict: A dictionary containing the article metadata.
    """

    url = f"https://api.crossref.org/works/{doi}"
    headers = {
        "User-Agent": "SCI4RAG/1.0 (mailto:sci_email@example.com)"
    }

    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    return r.json()["message"]

# Author Extraction
def extract_author(data: dict):
    authors = []
    for a in data.get("author", []):
        family = a.get("family", "").strip()
        given = a.get("given", "").strip()
        if family and given:
            authors.append(f"{given} {family}")
        elif family:
            authors.append(family)
        elif given:
            authors.append(given)
    return authors


# Journal Extraction
def extract_journal(data: dict):
    return (
        (data.get("container-title") or [None])[0]
        or (data.get("short-container-title") or [None])[0]
        or data.get("publisher")
    )

# Year Extraction
def extract_year(data: dict):
    for key in [
        "published-print",
        "published",
        "issued",
        "published-online",
        "created",
    ]:
        parts = data.get(key, {}).get("date-parts")
        if parts and parts[0] and parts[0][0]:
            return parts[0][0]
    return "XXXX"

# Volume Extraction
def extract_volume(data: dict):
    return data.get("volume")

# Issue Extraction
def extract_issue(data: dict):
    return (
        data.get("issue")
        or data.get("journal-issue", {}).get("issue")
    )

# Pages Extraction
def extract_pages(data: dict):
    return (
        data.get("page")
        or data.get("article-number")
        or data.get("eLocator")
    )

def make_citation_key(data: dict) -> str:
    """
    Generate a citation key for a given article metadata.

    Args:
        data (dict): The article metadata.

    Returns:
        str: The citation key.
    """
    authors = data.get("author", [])
    first_author = authors[0]["family"] if authors else "Unknown"

    year = extract_year(data)

    title_list = data.get("title", [""])
    title = title_list[0] if title_list else ""
    words = title.split()
    keyword = re.sub(r"\W+", "", words[0]) if words else "NoTitle"
    return f"{first_author}{year}{keyword}"

def to_custom_bibjson(data: dict) -> dict:
    """
    Convert article metadata to a custom BibJSON format.

    Args:
        data (dict): The article metadata.

    Returns:
        dict: The custom BibJSON format.
    """
    return {
            "title": data.get("title", [None])[0],
            "author": extract_author(data),
            "journal": extract_journal(data),
            "doi": data.get("DOI"),
            "url": data.get("URL"), 
            "year": extract_year(data),
            "volume": extract_volume(data),
            "number": extract_issue(data),
            "pages": extract_pages(data),
            "bibkey": make_citation_key(data),
        }

def get_doi_info(doi: str) -> dict:
    """
    Get article metadata from DOI.

    Args:
        doi (str): The DOI of the article.

    Returns:
        dict: The article metadata.
    """
    time.sleep(0.5)  # To avoid hitting rate limits
    raw = fetch_article_info_by_doi(doi)
    bibjson = to_custom_bibjson(raw)
    return bibjson

def identify_doi_info(file_data: dict) -> None:
    """
    Fetch article metadata by DOI and save it as a JSON file.

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
        path (str): The file path to save the JSON data.
    """
    if file_data["DOI_state"] in {
            "Doi_Info_Getted",
            "Doi_Updated"
        }:
        print(f"{file_data['file_name']}: Already {file_data['DOI_state']}, skip DOI identification")

    username, dataset_name = parse_path_info(file_data["file_path"])

    if "doi" not in file_data: 
        file_data["DOI_state"] = "Not_DOI"
        updata_document_metadata(username, dataset_name, file_data, info=False)
        file_data =  identify_DOI(file_data)

    if file_data["DOI_state"] == "Not_DOI":
        if file_data["doi"] in (None, "", "null", "Null", "NULL"):
            print(f"{file_data['file_name']}: DOI not found")
            return file_data
    
    doi_path = Path(
        f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/doi.json"
    )
    if not doi_path.exists():
        file_data["DOI_state"] = "Doi_Info_Getted"
        updata_document_metadata(username, dataset_name, file_data, info=False)
        bibjson = get_doi_info(file_data["doi"])
        save_json(bibjson, doi_path)
def load_doi_info(file_data: dict) -> dict:
    """
    Load article metadata from a JSON file.

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
        dict: The article metadata.
    """
    username, dataset_name = parse_path_info(file_data["file_path"])
    doi_path = Path(
        f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/doi.json"
    )
    if not doi_path.exists():
        raise FileNotFoundError(f"DOI info file not found: {doi_path}")
    return load_json(doi_path)

def safe_name(name: str) -> str:
    """Make a filesystem-safe name."""
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:150]  # Windows safety

def update_doc_info(username: str, dataset_name: str) -> None:
    """
    Update document metadata according to DOI information,
    including renaming the document key and name field.

    Args:
        username (str): The username of the user.
        dataset_name (str): The name of the dataset.

    Returns:
        None
    """
    base = Path("users") / username / dataset_name
    pdf_files_data = load_document_metadata(username, dataset_name)

    updated_pdf_files_data = {}

    for file_id, file_data in pdf_files_data.items():
        old_pdf = Path(file_data['file_path'])
        if not old_pdf.exists():
            print(f"[WARN] File not found: {old_pdf}")
            delete_file(file_data)
            continue

        if file_data["DOI_state"] in {
            "Doi_Updated",
        }:
            updated_pdf_files_data[file_id] = file_data
            continue
        
        doi = file_data.get("doi")
        if doi in (None, "", "null", "Null", "NULL"):
            updated_pdf_files_data[file_id] = file_data
            continue

        doi_data = load_doi_info(file_data)
        raw_title = doi_data.get("title")

        if not raw_title:
            updated_pdf_files_data[file_id] = file_data
            continue

        title = safe_name(raw_title)

        # ---- resolve key collision ----
        new_key = title

        # ---- rename pdf atomically ----

        new_pdf = base / "documents" / f"{new_key}.pdf"
        
        if old_pdf != new_pdf and new_pdf.exists():
                print(f"{new_pdf} already exists, delete this file")
                delete_file(file_data)
                continue

        old_pdf.rename(new_pdf)

        # ---- update metadata only AFTER rename ----
        file_data["DOI_state"] = "Doi_Updated"
        file_data["file_name"] = new_key
        file_data["file_path"] = str(new_pdf)
        updated_pdf_files_data[file_id] = file_data

    # ---- save metadata ----
    save_json(
        updated_pdf_files_data,
        base / "documents.json"
    )

def get_reference_info(reference: str) -> dict:
    """
    Get article metadata from reference.

    Args:
        reference (str): The reference of the article.

    Returns:
        dict: The article metadata.
    """
    time.sleep(0.5)  # To avoid hitting rate limits
    raw = query_crossref(reference)
    bibjson = to_custom_bibjson(raw)
    return bibjson

if __name__ == "__main__":
    doi = "10.1016/j.actamat.2024.120007"
    # print(fetch_article_info_by_doi(doi))
    bibjson = get_doi_info(doi)
    print(bibjson)

    # refer=   "J.D. Rittner, D.N. Seidman, K.L. Merkle, Grain-boundary dissociation by the emission of stacking faults, Phys. Rev. B 53 (8) (1996) R4241-R4244."
    # # print(query_crossref(refer))    
    # bibjson = to_custom_bibjson(query_crossref(refer))
    # print(bibjson)