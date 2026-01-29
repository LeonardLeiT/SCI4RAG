from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from .llm_model import get_chat_model
import os
import json
import shutil
from pathlib import Path
from datetime import datetime
import random

DATA_FILE = 'history.json'

def get_user_dir(username):
    """Get the user-specific directory path"""
    user_dir = f'users/{username}'
    Path(user_dir).mkdir(parents=True, exist_ok=True)
    return user_dir

def load_history_infos(username):
    """Load models for a specific user"""
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
    """Save models for a specific user"""
    user_dir = get_user_dir(username)
    file_path = os.path.join(user_dir, "history",DATA_FILE)
    
    with open(file_path, 'w') as f:
        json.dump(models, f, indent=4)

def delete_database(username, history_id):
    """Delete a specific model for a user"""
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
        with open(history_path, 'r', encoding='utf-8') as f:
            raw_history = json.load(f)
        history_messages = [
            HumanMessage(content=m["content"]) if m["type"] == "human" else AIMessage(content=m["content"])
            for m in raw_history
        ]
    else:
        history_messages = []
    history_path = f'users/{username}/history/{history_id}/{history_id}_sum.json'
    if os.path.exists(history_path):
        with open(history_path, 'r', encoding='utf-8') as f:
            raw_history = json.load(f)
        history_sum = [
            HumanMessage(content=m["content"]) if m["type"] == "human" else AIMessage(content=m["content"])
            for m in raw_history
        ]
    else:
        history_sum = []
    # PUT the history_id to the First
    history_infos = load_history_infos(username)
    if history_id in history_infos:
        target_item = history_infos.pop(history_id)
        updata_info = {history_id: target_item}
        updata_info.update(history_infos)
        save_history_infos(username, updata_info)
    return history_messages, history_sum

def updata_history(human_text, ai_text, history_messages):
    if human_text and ai_text:
        history_messages.append(HumanMessage(content=human_text))
        history_messages.append(AIMessage(content=ai_text)) 

def store_history(history_messages, history_id='First', username="12", custom = ''):
    if history_messages is None:
        return
    # Convert to serializable form
    serializable = [
        {"type": "human", "content": m.content} if isinstance(m, HumanMessage)
        else {"type": "ai", "content": m.content}
        for m in history_messages
    ]

    history_path = f'users/{username}/history/{history_id}/{history_id+custom}.json'
    os.makedirs(os.path.dirname(history_path), exist_ok=True)
    with open(history_path, 'w', encoding='utf-8') as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)

def prompt_history(prompt, history_messages):
    session_messages = []
    
    if prompt:
        session_messages.append(SystemMessage(content=prompt))
    
    session_messages.extend(history_messages)

    return session_messages

def summary_history(history_messages, llm, time = 15):
    # If chat is less than 15 messages (approx. 7 rounds), skip summarization
    if len(history_messages) < time * 2:
        return history_messages
    
    summary_time = 3
    # Separate the first 5 rounds: 5 human + 5 AI messages
    human_msgs = [m.content for m in history_messages[:summary_time*2] if isinstance(m, HumanMessage)]
    ai_msgs = [m.content for m in history_messages[:summary_time*2] if isinstance(m, AIMessage)]

    # Summarize human messages
    human_summary_prompt = [
        SystemMessage(content="Summarize the user's questions and inputs in a concise way:"),
        *[HumanMessage(content=msg) for msg in human_msgs]
    ]
    human_summary = llm.invoke(human_summary_prompt).content

    # Summarize AI messages
    ai_summary_prompt = [
        SystemMessage(content="Summarize the assistant's responses in a concise way:"),
        *[AIMessage(content=msg) for msg in ai_msgs]
    ]
    ai_summary = llm.invoke(ai_summary_prompt).content

    # Create summary messages
    summary_messages = [
        SystemMessage(content="Summary of earlier user inputs: " + human_summary),
        SystemMessage(content="Summary of earlier assistant responses: " + ai_summary)
    ]

    # Return the summarized + remaining messages
    return summary_messages + history_messages[summary_time*2:]

def chat_index(query, username, llm=None):
    if llm is None:
        llm = get_chat_model()
    prompt = f"""
    Please summarize the following query into a title, which should be a concise summary or clarification of the query.
    The title should be no more than 15 words and capture the main subject of the query. Just return the title name is ok. 

    Query: {query}
    """  
    response = llm.invoke(prompt)
    title = response.content.strip().split('\n')[0]
    title = title.replace('"', '').replace("'", "")
    now = datetime.now()
    formatted = now.strftime("%Y%m%d%H%M%S%f") 
    random_part = random.randint(100, 999) 
    history_id = f"{formatted}-{random_part}"
    history_infos = load_history_infos(username)
    history_infos[history_id] = {
        "history_title": title,
        "history_id": history_id
    }
    save_history_infos(username, history_infos)
    return history_id
  
if __name__ == "__main__":
    from llm_model import get_chat_model

    llm = get_chat_model()
    history_id = chat_index('what is topological defect?', '12', llm)
    print(history_id)
    # Load existing history
    history_messages, history_sum= initial_history('12', history_id)
    print(history_messages)
    store_history(history_messages, history_id)
    store_history(history_messages, history_id, custom='_sum')
    # print(prompt_history(prompt, history_messages))
    # Start chat loop
    print("Chat session started. Type 'exit' to quit.")
    user_input = None
    full_response = None
    prompt = "You are a chat assistant."  
    # prompt = SystemMessage(content=prompt)
    while True:
        # Update and possibly summarize history
        updata_history(user_input, full_response, history_messages)
        updata_history(user_input, full_response, history_sum)
        history_sum = summary_history(history_messages, llm, time=10)
        
        user_input = input("You: ")
        if user_input.lower() == "exit":
            store_history(history_messages, history_id)
            store_history(history_sum, history_id, custom='_sum')
            break

        # Compose full message list for context
        messages = prompt_history(prompt, history_sum)
        messages.append(HumanMessage(content=user_input))
        print("history:", len(history_messages)//2)

        # Stream AI response
        print("AI: ", end="", flush=True)
        full_response = ""
        for chunk in llm.stream(messages):
            print(chunk.content, end="", flush=True)
            full_response += chunk.content
        print()  # for newline
        
    print("Chat session ended.")

