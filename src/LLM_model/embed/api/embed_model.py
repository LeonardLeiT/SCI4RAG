import json
from pathlib import Path

from langchain_community.embeddings import (
    OpenAIEmbeddings,
    DashScopeEmbeddings,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "api_key"

def load_api_key(chatmodel="aliyun"):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if chatmodel not in data:
        raise KeyError(f"API key for '{chatmodel}' not found")

    return data[chatmodel]

# Define provider-specific constructor functions
def aliyun_embed_llm(modelType, apiKey):
    return DashScopeEmbeddings(
        model=modelType,
        dashscope_api_key=apiKey
    )

def openai_embed_llm(modelType, apiKey):
    return OpenAIEmbeddings(
        model=modelType,
        openai_api_key=apiKey
    )

# Dispatch map for providers
embedding_provider_map = {
    "aliyun": aliyun_embed_llm,
    "openai": openai_embed_llm,
}

# Unified getter function
def get_embed_model(embedmodel = "aliyun", modelType ="text-embedding-v1"):
    key = load_api_key(embedmodel)
    return embedding_provider_map[embedmodel](modelType = modelType, apiKey = key)

if __name__ == "__main__":
    print(get_embed_model())
