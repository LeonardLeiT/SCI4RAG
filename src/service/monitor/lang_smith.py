import os
from dotenv import load_dotenv

load_dotenv()

langsmith_key = os.getenv("LANGCHAIN_API_KEY")
def load_langsmith(project = 'test', switch = 1):
    if switch == 1:
        os.environ["LANGCHAIN_TRACING_V2"]="true"
    else:
        os.environ["LANGCHAIN_TRACING_V2"]="false" 
    os.environ["LANGCHAIN_PROJECT"]=project
    os.environ["LANGCHAIN_API_KEY"]=langsmith_key 
    os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com" 