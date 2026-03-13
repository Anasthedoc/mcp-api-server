from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

app = FastAPI()

llm = ChatOpenAI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/ask")
async def ask(prompt: str):
    response = llm.invoke(prompt)
    return {"response": response.content}
