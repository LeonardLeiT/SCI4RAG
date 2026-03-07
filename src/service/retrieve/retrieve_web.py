import json
from pathlib import Path
from serpapi import GoogleSearch
from ddgs import DDGS
from langchain_core.messages import SystemMessage

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "api_key"

def load_api_key(model="Google"):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if model not in data:
        raise KeyError(f"API key for '{model}' not found")

    return data[model]

def get_web_Google(query, result=10):
    params = {
        "q": query,
        "num": result,
        "api_key": load_api_key(model="Google"),
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    if "organic_results" not in results:
        return "Can't find in Google"

    prompt_parts = [f"Search results for: '{query}'\n"]
    for count, item in enumerate(results["organic_results"][:result], 1):
        title = item.get("title", "No Title")
        link = item.get("link", "No URL")
        snippet = item.get("snippet", "No summary available.")
        prompt_parts.append(f"{count}. {title}\nURL: {link}\nSummary: {snippet}\n")

    return "\n".join(prompt_parts)

def get_web_DDGS(query, results=5):
    results = DDGS().text(query, max_results = results)
    prompt_parts = [f"Search results for: '{query}'"]
    count = 0
    for r in results:
        link = r.get("href")  # DuckDuckGo uses 'href' for links
        if not link:
            continue
        title = r.get("title", "No title available")
        snippet = r.get("body", r.get("snippet", "No description available"))
        count += 1
        prompt_parts.append(f"{count}. {title}\nURL: {link}\nSummary: {snippet}\n")
    if count > 0:
        return "\n".join(prompt_parts)
    else: 
        return "Can't find in the wed DDGS"

# Dispatch map for web search methods
web_search_map = {
    "ddgs": get_web_DDGS,
    "google": get_web_Google,
    # Add more methods here if needed
}

# Unified web search getter
def get_web_message(
        query, 
        results=5, 
        max_retries=2, 
        method=None
        ):
    """
    web search getter

    Args:
        query (str): The query to search for.
        results (int, optional): The number of results to retrieve. Defaults to 5.
        max_retries (int, optional): The maximum number of retries to attempt. Defaults to 2.
        method (str, optional): The web search method to use. Defaults to None ['ddgs', 'google'].

    Returns:
        str: The web search results and urls.
    """
    if method:
        method = method.lower()
        if method not in web_search_map:
            raise ValueError(f"Unknown web search method: '{method}'. Choose from {list(web_search_map.keys())}")
        
        search_func = web_search_map[method]
        for attempt in range(max_retries):
            try:
                return search_func(query, results)
            except Exception as e:
                continue

        return f"Failed to fetch results after {max_retries} attempts using {method}."
    
    # --- If no method specified: try all search engines ---
    else:
        for name, search_func in web_search_map.items():
            for attempt in range(max_retries):
                try:
                    result = search_func(query, results)

                    if result and "Can't find" not in result:
                        return result

                except Exception:
                    continue

        return "Failed to fetch results from all available web search methods."

def web_prompt(
        query, 
        max_results = 5, 
        max_retries = 3,
        method = 'Google'
        ):
    """Construct a ChatPromptTemplate using retrieved context."""
    context = get_web_message(query, max_results, max_retries, method)

    # System prompt template
    system_template = f"""You are a helpful assistant specialized in question-answering tasks.
    Use the web search results below to answer the user's question.
    If the answer is not found in the context, respond with: "Web Searching can't find relevant knowledge."
    Provide a detailed and comprehensive answer.
    If the answer includes information from the context, clearly cite the source and include the relevant URL.
    ---------------------
    {context}
    """
    return system_template


if __name__ == "__main__":    
    # print(get_web_Google('LLM'))
    msg =  get_web_message('what is LLM', method='ddgs')
    print(msg)