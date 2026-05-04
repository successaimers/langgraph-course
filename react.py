from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from langchain_ollama import ChatOllama
MODEL = "qwen3:1.7b"
load_dotenv()

@tool
def triple(num:float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatOllama(model=MODEL, temperature=0).bind_tools(tools)

#llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)
