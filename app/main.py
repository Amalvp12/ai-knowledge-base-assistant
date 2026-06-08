from fastapi import FastAPI
from pydantic import BaseModel

from app.gemini_service import get_answer
from app.retriever import find_relevant_document

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Knowledge Base Assistant Running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    context = find_relevant_document(
        request.question
    )

    answer = get_answer(
        request.question,
        context
    )

    return {
        "answer": answer
    }