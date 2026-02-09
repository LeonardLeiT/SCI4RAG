import os
import json
import secrets
import shutil
from pathlib import Path
from glob import glob
from datetime import datetime


def save_json(data: dict, path: str, indent: int = 2, info = True) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)
    if info:
        print(f"JSON saved to: {path}")
def load_json(path: str) -> dict:
    """Load JSON file, return empty dict if not exists."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def load_document_metadata(username: str, dataset_name: str) -> dict:
    """
    Load the documents.json metadata file for a given user and dataset.
    """
    json_path = f"users/{username}/{dataset_name}/documents.json"
    return load_json(json_path)

def updata_document_metadata(username: str, dataset_name: str, metadata: dict, info = True) -> None:
    """
    update the documents.json metadata file for a given user and dataset.

    Args:
        username (str): The username of the user.
        dataset_name (str): The name of the dataset.
        metadata (dict): The metadata to update.
        info (bool, optional): Whether to print info message. Defaults to True.

    Returns:
        None
    """
    json_path = Path(f"users/{username}/{dataset_name}/documents.json")
    doc_info = load_json(json_path)
    doc_info[metadata["file_id"]] = metadata
    doc_info[metadata["file_id"]]["update_time"] = datetime.now().strftime("%a, %d %b %Y %H:%M")
    save_json(doc_info, json_path, info=info)

def parse_path_info(file_path: str):
    """
    Given a file path like:
    users\administrator\schwarz\documents\file.pdf
    Return (username, dataset_name)

    Args:
        file_path (str): The path to the file.

    Returns:
        tuple: (username, dataset_name)
    """
    parts = os.path.normpath(file_path).split(os.sep)

    # Expect format: users/<username>/<dataset>/documents/<filename>
    if len(parts) < 5 or parts[0] != "users" or parts[-2] != "documents":
        raise ValueError(f"Unexpected path format: {file_path}")

    username = parts[1]
    dataset_name = parts[2]
    return username, dataset_name

def load_PDF_file(username: str, dataset_name: str, file_path: str) -> dict:
    """
    Load a specific PDF file and update its metadata.

    Args:
        username (str): The username of the user.
        dataset_name (str): The name of the dataset.
        file_path (str): The path to the PDF file.

    Returns:
        dict: The metadata of the PDF file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    if not file_path.lower().endswith(".pdf"):
        raise ValueError(f"File is not a PDF: {file_path}")

    update_time = datetime.now().strftime("%a, %d %b %Y %H:%M")
    file_id = f"{datetime.now().strftime('%Y%m%dT%H%M%S')}_{secrets.token_hex(5)}"
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    file_meta = {
        "file_name": file_name,
        "file_type": "pdf",
        "file_path": file_path,
        "file_id": file_id,
        "file_size": file_size,
        "update_time": update_time,
        "parsing_status": "Not Parsed"  
    }

    json_path = f"users/{username}/{dataset_name}/documents.json"
    doc_info = load_json(json_path)

    # Check duplicate (same name + same size)
    for fid, meta in doc_info.items():
        if meta["file_name"] == file_name and meta["file_size"] == file_size:
            print(f"File already exists, skip: {file_name}")
            return meta

    # New file or updated file
    doc_info[file_id] = file_meta
    save_json(doc_info, json_path)

    print(f"Registered PDF: {file_name}")
    return file_meta

def load_Batch_PDF_files(username: str, dataset_name: str) -> dict:
    """
    Load all PDF files under users/<username>/<dataset_name>/documents

    Args:
        username (str): The username of the user.
        dataset_name (str): The name of the dataset.

    Returns:
        dict: The metadata of all PDF files.
    """
    pdf_dir = os.path.join("users", username, dataset_name, "documents")
    pdf_files = glob(os.path.join(pdf_dir, "*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in {pdf_dir}")

    print(f"Path: {pdf_dir}, Found {len(pdf_files)} PDF files.")

    for pdf in pdf_files:
        load_PDF_file(username, dataset_name, pdf)

    return load_json(f"users/{username}/{dataset_name}/documents.json")

def delete_file(file_data: dict) -> None:
    """
    Delete a file.    
    
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
    """
    file_path = Path(file_data["file_path"])
    username, dataset_name = parse_path_info(file_data["file_path"])
    base = Path("users") / username / dataset_name

    # 1. delete file_data["file_path"]
    if file_path.exists():
        file_path.unlink()
    # 2. delete username/dataset_name/parse/file_data["file_id"]
    file_id = file_data.get("file_id")
    parse_dir = base / "parse" / file_id
    if parse_dir.exists():
        shutil.rmtree(parse_dir, ignore_errors=True)    
    # 3. delete username/dataset_name/data_clean/file_data["file_id"]
    clean_dir = base / "data_clean" / file_id
    if clean_dir.exists():
        shutil.rmtree(clean_dir, ignore_errors=True)

def delete_none_dir(username: str, dataset_name: str) -> None:
    """
    Delete directories that do not have corresponding metadata.

    Args:
        username (str): The username of the user.
        dataset_name (str): The name of the dataset.
    """
    base = Path("users") / username / dataset_name
    data_info = load_document_metadata(username, dataset_name)

    # ---- parse ----
    parse_base = base / "parse"
    if parse_base.exists():
        for folder in parse_base.iterdir():
            if folder.is_dir() and folder.name not in data_info:
                print(f"[WARN] Orphan parse folder: {folder}")
                shutil.rmtree(folder, ignore_errors=True)

    # ---- data_clean ----
    clean_base = base / "data_clean"
    if clean_base.exists():
        for folder in clean_base.iterdir():
            if folder.is_dir() and folder.name not in data_info:
                print(f"[WARN] Orphan clean folder: {folder}")
                shutil.rmtree(folder, ignore_errors=True)


if __name__ == "__main__":
    username = "administrator"
    dataset_name = "schwarz"

    print("Preparing PDF files for MinerU processing...")
    pdf_files_data = load_Batch_PDF_files(username, dataset_name)
    print(f"Prepared {len(pdf_files_data)} files for upload.")
    for k, v in pdf_files_data.items():
        print(f"{k}: {v}")
