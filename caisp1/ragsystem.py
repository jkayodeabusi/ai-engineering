import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from openai import OpenAI   


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)


docs = ["AI is transforming the world", "LLMs are powerful"]

vectorstore = FAISS.from_texts(docs, OpenAIEmbeddings())

query = "What are LLMs?"
results = vectorstore.similarity_search(query)

print(results)