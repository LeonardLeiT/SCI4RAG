import os
import json
from pathlib import Path
from langchain_chroma import Chroma
from src.LLM_model.embed.api.embed_model import get_embed_model
from src.service.document.chunk_document import load_and_chunk_documents
from src.service.document.load_document import load_document_metadata, updata_document_metadata

def initialize_vector_store(
        username="administrator", 
        dataset_name='test'
        ):
    """
    Load and return an existing vector store collection

    Args:
        username: The username for the vector store.
        dataset_name: The name of the dataset.

    Returns:
        vector_store: The initialized vector store collection.    
    """
    vector_store = Chroma(
        collection_name=dataset_name,
        embedding_function=get_embed_model(),
        persist_directory=f"users/{username}/{dataset_name}/vector",
    )
    return vector_store

def add_documents_vector(vector_store, documents):
    vector_store.add_documents(documents=documents)

def delete_documents_vector(vector_store, source_name: str):
    """Delete documents that match a specific source"""
    vector_store.delete(where={"source": source_name})

def document_embedding(username="administrator", dataset_name="test"):
    pdf_files_data = load_document_metadata(username, dataset_name)

    pdf_files_sources = [
        f"users/{username}/{dataset_name}/data_clean/{file_id}/document.md"
        for file_id, file_data in pdf_files_data.items()
        # if not file_data.get("vector_status")
    ]

    all_splits = load_and_chunk_documents(pdf_files_sources)

    vector_store = initialize_vector_store(username, dataset_name)

    add_documents_vector(vector_store, all_splits)
