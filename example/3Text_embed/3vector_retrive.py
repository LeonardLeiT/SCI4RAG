from src.service.embed.vector_data import initialize_vector_store

username = "administrator"
dataset_name = "test"
print("Initializing vector store...")
vector_store = initialize_vector_store(username, dataset_name)
print("Vector store initialized.")
retrieved_docs = vector_store.similarity_search('SC', k=1)

print(retrieved_docs)
