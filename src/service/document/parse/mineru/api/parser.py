import os
import json
import time
import requests
import zipfile
from pathlib import Path
from datetime import datetime
from src.service.document.load_document import load_json, save_json, parse_path_info

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "api_key"

def load_api_key(model="mineru"):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if model not in data:
        raise KeyError(f"API key for '{model}' not found")

    return data[model]

# Configuration
API_TOKEN  = load_api_key()
batch_url = "https://mineru.net/api/v4/file-urls/batch"
MODEL_VERSION = "vlm"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}
def mineru_parse(file_data):
    if file_data["parsing_status"] != "Not Parsed":
        print(f"File already parsed or in progress: {file_data['file_name']}, status: {file_data['parsing_status']}")
        return 0
    
    data = {
        "files": [{
            "name": file_data["file_name"],
            "data_id": file_data["file_id"],
        }],
        "model_version": MODEL_VERSION
    }
    file_path = [file_data['file_path']]
    try:
        response = requests.post(batch_url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            print(f"{file_data['file_name']} response success.")
            if result["code"] == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                # print('batch_id:{}, urls:{}'.format(batch_id, urls))
                for i in range(0, len(urls)):
                    with open(file_path[i], 'rb') as f:
                        res_upload = requests.put(urls[i], data=f)
                        if res_upload.status_code == 200:
                            print(f"{file_data['file_name']} upload success")
                            username, dataset_name = parse_path_info(file_data["file_path"])
                            json_path = f"users/{username}/{dataset_name}/documents.json"
                            doc_info = load_json(json_path)
                            doc_info[file_data["file_id"]]["update_time"] = datetime.now().strftime("%a, %d %b %Y %H:%M")
                            doc_info[file_data["file_id"]]["parsing_status"] = "upload_success"
                            doc_info[file_data["file_id"]]["batch_id"] = batch_id
                            save_json(doc_info, json_path, info=False)
                        else:
                            print(f"{file_data['file_name']} upload failed")
            else:
                print('apply upload url failed,reason:{}'.format(result.msg))
        else:
            print('response not success. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)

def mineru_state(file_data):
    """
    Check MinerU parsing status, download, unzip, and clean up zip file.
    """
    if file_data.get("parsing_status") == "Download":
        print(f"File already parsed and the result is downloaded: {file_data['file_name']}")
        return 0
    time.sleep(0.5)
    batch_id = file_data.get('batch_id')
    if not batch_id:
        print(f"No batch_id found for {file_data['file_name']}, cannot check status.")
        return -1

    url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        data = res.json()["data"]['extract_result'][0]

        print(f"File parsing status: {data['state']}")

        username, dataset_name = parse_path_info(file_data["file_path"])
        json_path = os.path.join("users", username, dataset_name, "documents.json")
        doc_info = load_json(json_path)

        # Update JSON metadata
        doc_info[file_data["file_id"]]["update_time"] = datetime.now().strftime("%a, %d %b %Y %H:%M")
        doc_info[file_data["file_id"]]["parsing_status"] = data['state']

        # Only download if done and full_zip_url exists
        if data['state'] == 'done' and data.get('full_zip_url'):
            zip_url = data['full_zip_url']

            # Ensure download folder exists
            download_dir = os.path.join("users", username, dataset_name, "parse", file_data["file_id"])
            os.makedirs(download_dir, exist_ok=True)

            # Save zip file
            base_name = os.path.splitext(file_data["file_name"])[0]
            zip_path = os.path.join(download_dir, f"{base_name}.zip")

            response = requests.get(zip_url)
            if response.status_code == 200:
                with open(zip_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded zip for {file_data['file_name']} to {zip_path}")

                # Extract the zip
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(download_dir)
                print(f"Extracted {file_data['file_name']} into {download_dir}")

                # Delete the zip file
                os.remove(zip_path)
                print(f"Deleted zip file: {zip_path}")

                # Update JSON status
                doc_info[file_data["file_id"]]["parsing_status"] = "Download"
                save_json(doc_info, json_path)
            else:
                print(f"Failed to download zip for {file_data['file_name']}, status code: {response.status_code}")
        else:
            save_json(doc_info, json_path)

    except Exception as err:
        print(f"Error while processing {file_data['file_name']}: {err}")
