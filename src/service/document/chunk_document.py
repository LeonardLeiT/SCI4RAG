import logging
import os
os.environ["USER_AGENT"] = "SCI4RAG-bot/1.0"
import bs4
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyMuPDFLoader,
    TextLoader,
    JSONLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter, 
    MarkdownTextSplitter,
    RecursiveJsonSplitter
)

# Function to load and chunk json documents
def load_and_chunk_json(source, chunk_size=1500, chunk_overlap=300):
    try:
        loader = JSONLoader(source, jq_schema=".content")
        docs = loader.load()
        text_splitter = RecursiveJsonSplitter(chunk_size, chunk_overlap)
        return text_splitter.split_documents(docs)
    except Exception as e:
        logging.error(f"Error processing JSON file {source}: {e}")
        raise

# Function to load and chunk markdown documents
def load_and_chunk_markdown(source, chunk_size=1500, chunk_overlap=300):
    try:
        loader = TextLoader(source, encoding="utf-8")
        docs = loader.load()
        text_splitter = MarkdownTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return text_splitter.split_documents(docs)
    except Exception as e:
        logging.error(f"Error processing markdown file {source}: {e}")
        raise

# Function to load and chunk PDF documents
def load_and_chunk_pdf(source, chunk_size=1500, chunk_overlap=300):
    try:
        loader = PyMuPDFLoader(source)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
        return text_splitter.split_documents(docs)
    except Exception as e:
        logging.error(f"Error processing PDF file {source}: {e}")
        raise

# Function to load and chunk web documents
def load_and_chunk_web(source, chunk_size=1000, chunk_overlap=200):
    try:
        loader = WebBaseLoader(
            web_paths=(source,),
            bs_kwargs=dict(
                parse_only=bs4.SoupStrainer(
                    class_=("post-content", "post-title", "post-header")
                )
            ),
        )

        docs = loader.load()

        if isinstance(docs, list):
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
            return text_splitter.split_documents(docs)
        else:
            logging.error(f"Unexpected data format from loader: {type(docs)}")
            raise ValueError(f"Expected a list, but got {type(docs)}")

    except Exception as e:
        logging.error(f"Error processing web page {source}: {e}")
        raise

# Dispatcher function
def load_and_chunk_documents(sources, chunk_size=1200, chunk_overlap=300):
    all_chunks = []
    for source in sources:
        try:
            if source.endswith(".md"):
                chunks = load_and_chunk_markdown(source, chunk_size, chunk_overlap)
            elif source.endswith(".json"):
                chunks = load_and_chunk_json(source, chunk_size, chunk_overlap)
            elif source.endswith(".pdf"):
                chunks = load_and_chunk_pdf(source, chunk_size, chunk_overlap)
            elif source.startswith("http"):
                chunks = load_and_chunk_web(source, chunk_size, chunk_overlap)
            else:
                raise ValueError(f"Unsupported source type: {source}")
            all_chunks.extend(chunks)
        except Exception as e:
            logging.error(f"Error processing {source}: {e}")
    return all_chunks

# if __name__ == "__main__":
#     sources = [
#         "https://lilianweng.github.io/posts/2023-06-23-agent/",
#         # "some_file.pdf",
#         # "example.md"
#         # "example.json"
#     ]

#     all_splits = load_and_chunk_documents(sources)

#     for i, chunk in enumerate(all_splits[:2]):
#         print(f"\n--- Chunk {i+1} ---\n{chunk.page_content[:500]}")
