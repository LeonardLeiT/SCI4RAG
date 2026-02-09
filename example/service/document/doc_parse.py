from src.service.document.load_document import load_Batch_PDF_files
from src.service.document.parse.mineru.api.parser import mineru_parse, mineru_state

username = "administrator"
dataset_name = "test"

# 1.Load PDF files
pdf_files_data = load_Batch_PDF_files(username, dataset_name)

# 2.Start parsing
for file_id, file_data in pdf_files_data.items():
    mineru_parse(file_data)

# 3.Check parsing status (optional)
for file_id, file_data in pdf_files_data.items():
    mineru_state(file_data)

