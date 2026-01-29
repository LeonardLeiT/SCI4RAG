from langchain_openai import ChatOpenAI
from llm_model import get_chat_model

def rewrite_query_search(query: str, llm = get_chat_model()) -> list:
    # Define the prompt to rewrite the query into 3 key points, with an example to guide the model
    prompt = f"""
    Please rewrite the following query into 3 key points. Each point should be a concise summary or clarification of the query. For example:
    
    Query: "What are the benefits of machine learning?"
    Output:
    1. Key applications of machine learning in various industries.
    2. How machine learning helps automate tasks and improve efficiency.
    3. The potential impact of machine learning on future technology and jobs.
    
    Now, rewrite the following query into 3 key points:
    
    {query}
    """
    
    # Invoke the model with the prompt
    response = llm.invoke(prompt)
    
    # Extract the original query and the structured points
    output = response.content.strip().split('\n')
    
    # The first entry in the output is the original query (we can keep it as a separate item)
    original_query = query
    
    # The subsequent lines should be the rewritten points (1-3)
    rewritten_points = [output[i].strip() for i in range(0, len(output))]

    # Store them as a list, keeping them separate
    full_output = [original_query] + rewritten_points  # The list will start with the query followed by the 3 points

    return full_output

if __name__ == "__main__":
    # Example usage
    query = "What are the latest advancements in quantum computing?"
    result = rewrite_query_search(query)
    for i in result:
        print(i)   



