from fastapi import FastAPI
from pydantic import BaseModel
from core.pipeline import revision_pipeline

app = FastAPI()

class RevisionRequest(BaseModel):    
    text: str

@app.post("/revision")
def revision(request: RevisionRequest):
    text = request.text.strip()
    if len(text) < 5 or not any(char.isalpha() for char in text):
        return {"error": "Meaningful educational text required."} 
    result = revision_pipeline(text)
    return result