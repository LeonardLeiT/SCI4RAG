from src.service.document.load_document import load_document_metadata
from src.service.document.clean_markdown import identify_main_section, combile_doc_json, combine_label_structure, identify_detail

username = "administrator"
dataset_name = "test"

# 1.Load documents Information
pdf_files_data = load_document_metadata(username, dataset_name)

# 2.Load Markdown and identify chunks main sections
for file_id, file_data in pdf_files_data.items():
    identify_main_section(file_data)
    identify_detail(file_data)

# 3.Combile Documents
for file_id, file_data in pdf_files_data.items():
    combine_label_structure(file_data)
    combile_doc_json(file_data)