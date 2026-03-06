from src.service.document.load_document import load_document_metadata
from src.service.document.chunk_document import load_and_chunk_documents    

username = "administrator"
dataset_name = "test"

# Step 1: Chunk Documents
# Run:  python -m example.3Text_embed.1doc_chunk

# 1.Load documents Information
pdf_files_data = load_document_metadata(username, dataset_name)

pdf_files_sources = [
    f"users/{username}/{dataset_name}/data_clean/{file_id}/document.md"
    for file_id, file_data in pdf_files_data.items()
    # if not file_data.get("vector_status")
]

print(len(pdf_files_sources), "files to chunk")
print(pdf_files_sources)

# 2. Chunk documents and prepare for embedding
all_splits = load_and_chunk_documents(pdf_files_sources)
print(f"Total chunks created: {len(all_splits)}")
print(all_splits)