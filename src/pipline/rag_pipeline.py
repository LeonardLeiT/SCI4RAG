import sys
from pathlib import Path
from langchain_core.messages import HumanMessage
# Add the project root directory to the Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from retriever.vector_store import initialize_vector_store, load_database
from retriever.retriever import retriever_prompt
from generator.llm_model import get_chat_model
from retriever.embed_model import get_embedding_model
from generator.history_tree_chat import (
    initial_history,
    store_history,
    prompt_history,
    updata_history,
)
from generator.history_tree import Role

class RAGPipeline:
    def __init__(
        self,
        prompt: str = "Your name is SchwarzRag. You are a helpful assistant. Provide a detailed and comprehensive answer.",
        temperature: float = 0.7,
        max_tokens: int = 4096,
        use_stream: bool = True,
        username="12",
        model_name = '12',
        dataset_name = 'Schwarz',
        num_retrieved_docs = 5,
        history_id: str = 'First',
    ):
        """Initialize the RAG pipeline."""
        self.prompt = prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.use_stream = use_stream
        self.username = username
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.num_retrieved_docs = num_retrieved_docs
        self.history_id = history_id

        self.llm = get_chat_model(
            username=self.username,
            model_name=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        self.tree, self.current_node_id = initial_history(
            username=self.username,
            history_id=self.history_id
        )
        
        self.model = load_database(self.username, self.dataset_name)   

        self.embedding = get_embedding_model(
            username = self.username,
            embed_name = self.model['embedmodel']
        )
        
        self.vector_store = initialize_vector_store(
            embeddings=self.embedding,
            store_name=self.dataset_name,
            username = self.username
        )    

    def query(self, query: str, Regenerate = 0, target_node_id = None):
        # Regenerate = 0 Status chat: Normal chat with LLM
        # Regenerate = 1 Status branch: New Question or Rewrite the answer

        # Handle branching to specific node
        if Regenerate == 1:
            node_id = target_node_id
            if node_id in self.tree:
                node = self.tree.get_node(node_id)
                if node and node.parent:
                    self.current_node_id = node.parent.id
                    if node.role == Role.USER:
                        Regenerate = 0
                        print("New question for this branch")
                    else:
                        print("Rewrite the question")
                        query = self.tree.get_node(self.current_node_id).message
                        Regenerate = 1
                else:
                    return "Node ID not found or invalid. Please try again."
            else:
                return "Node ID not found. Please try again."

        """Query the RAG pipeline."""
        rag_prompt = retriever_prompt(
            query,
            self.vector_store,
            self.num_retrieved_docs
        )
        messages = prompt_history(rag_prompt, self.tree, self.current_node_id)
        messages.append(HumanMessage(content=query))

        full_response = ""
        if self.use_stream:
            for chunk in self.llm.stream(messages):
                full_response += chunk.content
                yield chunk.content
            
            # Update conversation history
            self.current_node_id = updata_history(
                query, 
                full_response, 
                self.tree, 
                self.current_node_id, 
                Regenerate
            )
            
            # Auto-save after each interaction
            store_history(
                tree=self.tree,
                username=self.username,
                history_id=self.history_id,
                history_node_id=self.current_node_id
            )
        else:
            response = self.llm.invoke(messages)
            self.current_node_id = updata_history(
                query, 
                response.content, 
                self.tree, 
                self.current_node_id, 
                Regenerate
            )
            
            store_history(
                tree=self.tree,
                username=self.username,
                history_id=self.history_id,
                history_node_id=self.current_node_id
            )
            return response.content

if __name__ == "__main__":
    pipeline = RAGPipeline(
        temperature=0.7,
        max_tokens=4096,
        use_stream=True,
        dataset_name = 'Schwarz',
        history_id='20250524210004414717-681'
    )
    print("Chat session started. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Response: ", end="", flush=True)
        for chunk in pipeline.query(str(user_input)):
            print(chunk, end="", flush=True)
        print("")
        
    print("Chat session ended.")


