from langchain_classic import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq

# llm = ChatOpenAI(temperature=0)
# llm = ChatOllama(model="qwen3:0.6B", temperature=0)
llm = ChatGroq(model="gpt-oss-20b", temperature=0)
prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()


