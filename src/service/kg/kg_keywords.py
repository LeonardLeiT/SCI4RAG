import re
from pathlib import Path
from src.service.generator.llm_response import llm_response
from src.service.document.load_document import load_json, save_json, parse_path_info, updata_document_metadata


def generate_keyword_kg_article(
        title: str, 
        abstract: str,
        content: str, 
        temperature: float = 0.8
    ) -> dict:
    """
    Generate keywords in the file.

    Args:
        title (str): The title of the file.
        abstract (str): The abstract of the file.
        content (str): The content of the file.
        temperature (float, optional): The temperature of the LLM. Defaults to 0.8.

    Returns:
        str: The keywords of the article.
    """

    system_prompt = (

    )

    response = llm_response(
        query=equation,
        system_prompt=system_prompt,
        temperature=temperature
    ).strip()

    if response.lower() == "not clear" or  response.lower() == "not clear." or len(response.strip().split()) < 5:
        return None

    return 