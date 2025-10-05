from fastapi import FastAPI
from pydantic import BaseModel
from ollama_client import OllamaClient
import save_to_s3

class Prompt(BaseModel):
    content: str

app = FastAPI()

@app.post("/prompt/")
async def create_prompt(prompt: Prompt):
    result = process_prompt(prompt.content)
    save_to_s3.add_object_to_bucket(resume=result)
    return result

def process_prompt(content):
    client = OllamaClient(content=content)
    print(content)
    result = client.process_prompt()
    return result
