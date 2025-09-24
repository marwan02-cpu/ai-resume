from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Prompt(BaseModel):
    content: str

app = FastAPI()

@app.post("/prompt/")
async def create_item(prompt: Prompt):
    return prompt
