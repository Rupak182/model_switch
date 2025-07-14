from fastapi import FastAPI
from pydantic import BaseModel
from generate import generate  
class PromptRequest(BaseModel):
    message: str
    model: str = 'gptj'



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/generate")
def generate_response(prompt,model: str = 'gptj'):
    response= generate(prompt,model)


    return {"response": response}