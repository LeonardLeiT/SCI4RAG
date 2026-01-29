import json
from pathlib import Path

from langchain_openai import ChatOpenAI

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "api_key"

def load_api_key(chatmodel="deepseek"):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if chatmodel not in data:
        raise KeyError(f"API key for '{chatmodel}' not found")

    return data[chatmodel]

# Define provider-specific constructor functions
def aliyun_chat_llm(modelType, apiKey, temperature=1.0, max_tokens=4096):
    return ChatOpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key=apiKey,
        model=modelType,
        temperature=temperature,
        max_tokens=max_tokens,
        request_timeout=120,
        max_retries=3
    )

def deepseek_chat_llm(modelType, apiKey, temperature=0.7, max_tokens=4096):
    return ChatOpenAI(
        base_url="https://api.deepseek.com/v1",
        api_key=apiKey,
        model=modelType,
        temperature=temperature,
        max_tokens=max_tokens,
        request_timeout=120,
        max_retries=3
    )

# Dispatch map for providers
chat_provider_map = {
    "aliyun": aliyun_chat_llm,
    "deepseek": deepseek_chat_llm,
    # Add more providers here
}

# Unified getter function
def get_chat_model(chatmodel = "deepseek", modelType ="deepseek-chat", temperature=0.7, max_tokens=4096):
    key = load_api_key(chatmodel)
    return chat_provider_map[chatmodel](modelType = modelType, apiKey = key, temperature=temperature, max_tokens=max_tokens)

if __name__ == "__main__":  
    print(get_chat_model())