from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from ollama_client import OllamaClient

class Prompt(BaseModel):
    content: str

app = FastAPI()

@app.post("/prompt/")
async def create_prompt(prompt: Prompt):
    result = process_prompt(prompt.content)
    return result

def process_prompt(content):
    client = OllamaClient(content=content)
    result = client.process_prompt()
    print(result)
    return result
