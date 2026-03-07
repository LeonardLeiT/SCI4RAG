from pathlib import Path
from src.service.document.load_document import load_json, save_json

path = "config.json"

# Load configuration
data  = load_json(path)

# 1. Create chatmodel llm
chatmodel = data['chatmodel']
if chatmodel:
    if chatmodel['method'] == "api":
        name = chatmodel['name']
        modelType = chatmodel['modelType']
        apiKey = chatmodel['apiKey']
        chat_path = Path(
            f"src/LLM_model/chat/api/api_key"
            )
        {"name": name, "modelType": modelType, "apiKey": apiKey}
        save_json({"llm": name, "modelType": modelType, "apiKey": apiKey}, chat_path)

# 2. Create embedding model
embedmodel = data['embedmodel']
if embedmodel:
    if embedmodel['method'] == "api":
        name = embedmodel['name']
        modelType = embedmodel['modelType']
        apiKey = embedmodel['apiKey']
        embed_path = Path(
            f"src/LLM_model/embed/api/api_key"
            )
        save_json({"embed": name, "modelType": modelType, "apiKey": apiKey}, embed_path)

# 3. Create parser model
mineru = data['mineru']
if mineru:
    if mineru['method'] == "api":
        apiKey = mineru['apiKey']
        mineru_path = Path(
            f"src/service/document/parse/mineru/api/api_key"
            )
        save_json({"mineru": apiKey}, mineru_path)

# 4. Create web search model of Google
Google = data['google_web_search']
if Google:
    if Google['method'] == "api":
        apiKey = Google['apiKey']
        web_path = Path(
            f"src/service/retrieve/api_key"
            )
        save_json({"Google": apiKey}, web_path)