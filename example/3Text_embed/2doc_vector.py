from src.service.embed.vector_data import document_embedding

username = "administrator"
dataset_name = "test"

# Step 2: Create Vector Embeddings
# Run:  python -m example.3Text_embed.2doc_vector
print("Starting document embedding...")
document_embedding(username, dataset_name)
print("Starting document embedding...")
# exist_docs = check_documents_exist(username, dataset_name)
# print(exist_docs)
# if exist_docs:
#     print("Documents exist in the vector store.")
#     print(f"Existing sources: {exist_docs}")
# else:
#     print("Documents do not exist in the vector store.")