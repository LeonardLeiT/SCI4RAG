from langchain_core.messages import HumanMessage, SystemMessage
from src.LLM_model.chat.api.llm_model import get_chat_model
from src.service.embed.vector_store import initialize_vector_store
from src.service.retrieve.retrieve_vector import retrieve_prompt

class RAGPipeline:
    def __init__(
        self,
        prompt: str = "Your name is SchwarzRag. You are a helpful assistant. Provide a detailed and comprehensive answer.",
        temperature: float = 0.7,
        max_tokens: int = 4096,
        username="administrator",
        dataset_name = "test",
        num_retrieved_docs = 5,
    ):
        """Initialize the RAG pipeline."""
        self.prompt = prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.username = username
        self.dataset_name = dataset_name
        self.num_retrieved_docs = num_retrieved_docs

        self.llm = get_chat_model(
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        self.vector_store = initialize_vector_store(
            username=self.username,
            dataset_name=self.dataset_name
        )    

    def build_messages(self, query: str):
        """Construct RAG prompt messages."""
        rag_prompt = retrieve_prompt(
            query,
            self.vector_store,
            self.num_retrieved_docs
        )

        return [
            SystemMessage(content=self.prompt + rag_prompt),
            HumanMessage(content=query),
        ]

    def query(self, query: str):
        """Non-streaming response."""
        messages = self.build_messages(query)
        response = self.llm.invoke(messages)
        return response.content

    def query_stream(self, query: str):
        """Streaming response."""
        messages = self.build_messages(query)
        for chunk in self.llm.stream(messages):
            yield chunk.content

if __name__ == "__main__":
    pipeline = RAGPipeline(
        temperature=0.7,
        max_tokens=4096,
        username="administrator",
        dataset_name = 'test',
    )
    print("Chat session started. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Response: ", end="", flush=True)
        for chunk in pipeline.query_stream(str(user_input)):
            print(chunk, end="", flush=True)
        print("")
        
    print("Chat session ended.")


