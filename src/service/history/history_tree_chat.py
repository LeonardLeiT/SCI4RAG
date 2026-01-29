from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from .llm_model import get_chat_model
import os
import json
import shutil
from pathlib import Path
from datetime import datetime
import random
from .history_tree import DialogueTree, Role

DATA_FILE = 'history.json'

def get_user_dir(username):
    user_dir = f'users/{username}'
    Path(user_dir).mkdir(parents=True, exist_ok=True)
    return user_dir

def load_history_infos(username):
    user_dir = get_user_dir(username)
    file_path = os.path.join(user_dir, "history", DATA_FILE)
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def load_history_info(username, history_id):
    models = load_history_infos(username)
    if history_id in models:
        return models[history_id]
    else:
        print("Can't find history information !!")
        return False

def save_history_infos(username, models):
    user_dir = get_user_dir(username)
    file_path = os.path.join(user_dir, "history", DATA_FILE)
    with open(file_path, 'w') as f:
        json.dump(models, f, indent=4)

def delete_database(username, history_id):
    models = load_history_infos(username)
    if history_id in models:
        del models[history_id]
        save_history_infos(username, models)
        folder_path = os.path.join("users", username, "history", history_id)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        return True
    return False

def initial_history(username="12", history_id='First'):
    history_path = f'users/{username}/history/{history_id}/{history_id}.json'
    if os.path.exists(history_path):
        tree = DialogueTree.from_json(history_path)
        model = load_history_info('12', history_id)
        current_node_id = model["history_node_id"]
    else:
        tree = DialogueTree()
        current_node_id = None
    return tree, current_node_id

def updata_history(human_text, ai_text, tree: DialogueTree, last_node_id: str = None, Regenerate = 0):
    if human_text and ai_text:
        if Regenerate == 0:
            human_node = tree.add_node(Role.USER, human_text, last_node_id)
            ai_node = tree.add_node(Role.ASSISTANT, ai_text, human_node.id)
        else:
            ai_node = tree.add_node(Role.ASSISTANT, ai_text, last_node_id)
        return ai_node.id
    return last_node_id

def store_history(tree: DialogueTree, username="12",  history_id='First', history_node_id=None):
    history_path = f'users/{username}/history/{history_id}/{history_id}.json'
    os.makedirs(os.path.dirname(history_path), exist_ok=True)
    tree.to_json(history_path) 
    history_infos = load_history_infos(username)
    history_infos[history_id]["history_node_id"] = history_node_id
    save_history_infos(username, history_infos)

def prompt_history(prompt, tree: DialogueTree, node_id: str):
    session_messages = []
    if prompt:
        session_messages.append(SystemMessage(content=prompt))

    if node_id in tree:
        msgs = tree.get_full_context(node_id)
        for msg in msgs:
            role, content = msg.split(": ", 1)
            if role == "USER":
                session_messages.append(HumanMessage(content=content))
            else:
                session_messages.append(AIMessage(content=content))
    return session_messages

def chat_index(query, username, llm=None):
    if llm is None:
        llm = get_chat_model()
    prompt = f"""
    Please summarize the following query into a title, which should be a concise summary or clarification of the query.
    The title should be no more than 15 words and capture the main subject of the query. Just return the title name is ok. 

    Query: {query}
    """  
    response = llm.invoke(prompt)
    title = response.content.strip().split('\n')[0].replace('"', '').replace("'", "")
    now = datetime.now()
    formatted = now.strftime("%Y%m%d%H%M%S%f") 
    random_part = random.randint(100, 999) 
    history_id = f"{formatted}-{random_part}"
    history_infos = load_history_infos(username)
    history_infos[history_id] = {
        "history_title": title,
        "history_id": history_id,
        "history_node_id": None
    }
    save_history_infos(username, history_infos)
    return history_id

if __name__ == "__main__":
    llm = get_chat_model()
    # history_id = chat_index('what is topological defect?', '12', llm)
    history_id = '20250524210004414717-681'
    tree, current_node_id = initial_history('12', history_id)
    prompt = "You are a chat assistant."

    print("Chat session started. Type 'exit' to quit.")
    while True:
        Regenerate = 0
        user_input = input("You: ")
        if user_input.lower() == "exit":
            store_history(tree, "12", history_id, current_node_id)
            break
        
        # Allow branching
        if user_input.lower() == "branch":
            print("Starting branch...")
            new_id = "83d7fcb6-7e32-4023-ac8f-4e27ccfb5abe"
            print(new_id)
            if new_id in tree:
                node = tree.get_node(new_id)
                print(node.role)
                if node and node.parent:
                    current_node_id = node.parent.id
                    if node.role == Role.USER:
                        print("Please write your question")
                        user_input = input("You: ")
                    else:
                        user_input = tree.get_node(current_node_id).message
                        Regenerate = 1                        
                else:
                    print("Node ID not found. Please try again.")
                    continue

        messages = prompt_history(prompt, tree, current_node_id)
        messages.append(HumanMessage(content=user_input))
        print(user_input)

        print("AI: ", end="", flush=True)
        full_response = ""
        for chunk in llm.stream(messages):
            print(chunk.content, end="", flush=True)
            full_response += chunk.content
        print()


        current_node_id = updata_history(user_input, full_response, tree, current_node_id, Regenerate)

    print("Chat session ended.")
