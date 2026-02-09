from src.service.agent.identify_reference import process_references
from src.service.agent.identify_figure import process_figures
from src.service.agent.identify_equation import identify_equation
from src.service.document.load_document import load_document_metadata

username = "administrator"
dataset_name = "test"
print("Loading documents metadata...")

# 1.Load documents Information
pdf_files_data = load_document_metadata(username, dataset_name)

# 4.identify equations and references
for file_id, file_data in pdf_files_data.items():
    print(f"Identifying equations and references for {file_data['file_name']}...")
    identify_equation(file_data)
    process_references(file_data)
    process_figures(file_data)