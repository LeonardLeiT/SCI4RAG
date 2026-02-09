from src.LLM_model.chat.api.llm_model import get_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
def llm_response(query: str,
                 system_prompt: str = "",
                 temperature: float = 1,
    ) -> str:
    """
    Call the LLM with a system prompt and user query, returning a cleaned string response.

    Args:
        query : str
            The user text
        system_prompt : str
            System instructions for the model.
        temperature : float
            Sampling temperature (0 = deterministic).

    Returns:
        str
            The LLM output, stripped and lowercased.
    """

    llm=get_chat_model(temperature=temperature)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]
    return llm.invoke(messages).content