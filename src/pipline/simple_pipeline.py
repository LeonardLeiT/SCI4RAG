from langchain_core.messages import HumanMessage, SystemMessage
from src.LLM_model.chat.api.llm_model import get_chat_model

class SimplePipeline:
    def __init__(
        self,
        prompt: str = "Your name is SchwarzRag. You are a helpful assistant. Provide a detailed and comprehensive answer.",
        temperature: float = 0.7,
        max_tokens: int = 4096,
        username="administrator",
    ):
        """Initialize the Simple pipeline."""
        self.prompt = prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.username = username

        self.llm = get_chat_model(
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

    def build_messages(self, query: str):
        """Construct prompt messages."""
        return [
            SystemMessage(content=self.prompt),
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
    pipeline = SimplePipeline(
        temperature=0.7,
        max_tokens=4096,
    )
    # targer_id = "83d7fcb6-7e32-4023-ac8f-4e27ccfb5abe"
    user_input = 'Can you search in the web'
    print("Response: ", end="", flush=True)
    for chunk in pipeline.query_stream(user_input):
        print(chunk, end="", flush=True)
    print("")
