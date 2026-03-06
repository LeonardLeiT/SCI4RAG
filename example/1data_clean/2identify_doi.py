from src.service.document.load_document import load_document_metadata
from src.service.agent.article_information import identify_doi_info, identify_DOI, update_doc_info
from src.service.agent.identify_title import identify_title

username = "administrator"
dataset_name = "test"

# Step 2: Get Doi and Doi Information
# Run:  python -m example.1data_clean.2identify_doi

# 1.Load documents Information
pdf_files_data = load_document_metadata(username, dataset_name)

# 2.Get Scientific Letter Doi
for file_id, file_data in pdf_files_data.items():
    identify_DOI(file_data)

# 3.Get Doi Information
pdf_files_data = load_document_metadata(username, dataset_name)
i = 1
for file_id, file_data in pdf_files_data.items():
    if file_data["doi"]:
        # print(file_data["doi"])
        # print(f"Processing {i}: {file_data['file_name']}")
        # i += 1
        identify_doi_info(file_data)


# 4. Second Strategy for null doi
for file_id, file_data in pdf_files_data.items():
    if not file_data["doi"]:
        print(f"Processing {file_data['file_name']}")
        identify_title(file_data)

update_doc_info(username, dataset_name)