import sys
from pathlib import Path
from langchain_core.messages import HumanMessage, SystemMessage
# Add the project root directory to the Python path
project_root = str(Path(__file__).parent.parent)
print(project_root)
sys.path.append(project_root)

from LLM_model.chat.api.llm_model import get_chat_model

class SimplePipeline:
    def __init__(
        self,
        prompt: str = "Your name is SchwarzRag. You are a helpful assistant. Provide a detailed and comprehensive answer.",
        temperature: float = 0.7,
        max_tokens: int = 4096,
        use_stream: bool = True,
        username="administrator",
    ):
        """Initialize the Simple pipeline."""
        self.prompt = prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.use_stream = use_stream
        self.username = username

        self.llm = get_chat_model(
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

    def query(self, query: str):
        messages = [
            SystemMessage(content=self.prompt),
            HumanMessage(content=query),
        ]

        full_response = ""
        if self.use_stream:
            for chunk in self.llm.stream(messages):
                full_response += chunk.content
                yield chunk.content

        else:
            response = self.llm.invoke(messages)
            return response.content


if __name__ == "__main__":
    pipeline = SimplePipeline(
        temperature=0.7,
        max_tokens=4096,
        use_stream=True,
    )
    # targer_id = "83d7fcb6-7e32-4023-ac8f-4e27ccfb5abe"
    user_input = 'Can you search in the web'
    print("Response: ", end="", flush=True)
    for chunk in pipeline.query(user_input):
        print(chunk, end="", flush=True)
    print("")
