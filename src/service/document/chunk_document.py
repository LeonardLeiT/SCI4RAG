import logging
import os
import bs4
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyMuPDFLoader,
    TextLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownTextSplitter


# Configure logging to only capture errors
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# Function to load and chunk markdown documents
def load_and_chunk_markdown(source, chunk_size=1500, chunk_overlap=300):
    try:
        loader = TextLoader(source, encoding="utf-8")
        docs = loader.load()
        text_splitter = MarkdownTextSplitter(chunk_size, chunk_overlap)
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
            text_splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
            return text_splitter.split_documents(docs)
        else:
            logging.error(f"Unexpected data format from loader: {type(docs)}")
            raise ValueError(f"Expected a list, but got {type(docs)}")
    except Exception as e:
        logging.error(f"Error processing web page {source}: {e}")
        raise

# Dispatcher function
def load_and_chunk_documents(sources, chunk_size=None, chunk_overlap=None):
    all_chunks = []
    for source in sources:
        try:
            if source.endswith(".md"):
                chunks = load_and_chunk_markdown(source, chunk_size, chunk_overlap)
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

if __name__ == "__main__":
    sources = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        # "some_file.pdf",
        # "example.md"
    ]
    
    all_splits = load_and_chunk_documents(sources)

    for i, chunk in enumerate(all_splits[:2]):
        print(f"\n--- Chunk {i+1} ---\n{chunk.page_content[:500]}")
