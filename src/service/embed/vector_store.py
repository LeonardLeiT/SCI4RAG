import os
import json
from pathlib import Path
from langchain_chroma import Chroma
from .embed_model import get_embedding_model
from .load_document import load_and_chunk_documents

DATA_FILE = 'database.json'

def get_user_dir(username):
    """Get the user-specific directory path"""
    user_dir = f'users/{username}'
    Path(user_dir).mkdir(parents=True, exist_ok=True)
    return user_dir

def load_databases(username):
    """Load models for a specific user"""
    user_dir = get_user_dir(username)
    file_path = os.path.join(user_dir, DATA_FILE)
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def load_database(username, database_name):
    models = load_databases(username)
    if database_name in models:
        return models[database_name]
    else:
        print("Can't find Kownledage database !!")
        return False

def exist_store(user_id="system"):
    # Get path to the project root (one level above this file's folder)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    base_path = os.path.join(project_root, "users", user_id)
    datasets = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    return datasets

def check_store(user_id, store_name):
    # Get path to the project root (one level above this file's folder)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    base_path = os.path.join(project_root, "users", user_id)
    store_path = os.path.join(base_path, store_name)

    if os.path.exists(store_path):
        return store_name
    else:
        if os.path.exists(base_path):
            datasets = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
            raise ValueError(f"Store '{store_name}' not found. Available datasets: {datasets}")
        else:
            raise ValueError(f"Store '{store_name}' not found. No datasets available.")

def initialize_vector_store(embeddings, username="system", store_name='Lei'):
    """Load and return an existing vector store collection"""
    vector_store = Chroma(
        collection_name=store_name,
        embedding_function=embeddings,
        persist_directory=f"users/{username}/{store_name}/store",
    )
    return vector_store

def check_documents_exist(vector_store, documents):
    """Check which documents already exist in the vector store by their source."""
    existing_sources = set()
    if vector_store._collection.count() > 0:
        existing_metadata = vector_store._collection.get(include=["metadatas"])["metadatas"]
        existing_sources = {meta["source"] for meta in existing_metadata if "source" in meta}
    new_documents = [doc for doc in documents if doc.metadata.get("source") not in existing_sources]
    return existing_sources, new_documents

def add_documents_vector(vector_store, documents):
    """Add documents with source metadata"""
    vector_store.add_documents(documents)

def delete_documents_vector(vector_store, source_name: str):
    """Delete documents that match a specific source"""
    vector_store.delete(where={"source": source_name})

def get_vector_store(all_splits, embeddings=None, user_id="system", store_name='Lei'):
    """Initialize and return the vector store"""
    if embeddings is None:
        embeddings = get_embedding_model()
    vector_store = initialize_vector_store(embeddings, user_id, store_name)
    existing_sources, new_docs = check_documents_exist(vector_store, all_splits)
    if new_docs:
        add_documents_vector(vector_store, new_docs)
        new_sources = {doc.metadata.get("source") for doc in new_docs if "source" in doc.metadata}
        existing_sources.update(new_sources)
    return vector_store, existing_sources

def document_embedding(sources, user_name="12", dataset_name='embedded', embeddings = None):
    try:
        all_splits = load_and_chunk_documents(sources)
        vector_store, source_embed = get_vector_store(all_splits, embeddings, user_id=user_name, store_name=dataset_name)
        return vector_store, source_embed
    except:
        print('error when embedding')
        return False
    
if __name__ == "__main__":
    from langchain.schema import Document
    from load_document import load_and_chunk_documents
    
    # embed = get_embedding_model('12', '12')
    # initialize_vector_store(embed, '12', 'embedded')
    sources = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        # "some_file.pdf",
        # "example.md"
    ]
    
    all_splits = load_and_chunk_documents(sources)
    # all_splits
    # all_splits = [
    #     Document(page_content="This is document 3", metadata={"source": "doc3.txt"}),
    #     # Document(page_content="This is document 2", metadata={"source": "doc2.txt"})
    # ]
    

    vector_store, source = get_vector_store(all_splits, store_name='embedded', user_id="12")
    print(f"Loaded vector store with existing sources: {source}")
    vector_store, source = document_embedding(sources, user_name="12", dataset_name='embedded')
    print(f"Loaded vector store with existing sources: {source}")
    check_store('12', 'hihi')
    print('Hihi')