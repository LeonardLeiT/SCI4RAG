from src.service.embed.vector_store import initialize_vector_store
from src.service.retrieve.retrieve_vector import retrieve_prompt


# Step 3: Retrieve context with the similarity score
# Run:  python -m example.3Text_embed.3vector_retrive

username = "administrator"
dataset_name = "test"

# 1. Initialize vector store
print("Initializing vector store...")
vector_store = initialize_vector_store(username, dataset_name)

# 2. Retrieve
query = "What is the SC?"
retrieved_docs = retrieve_prompt(query, vector_store, 1)
print(retrieved_docs)
