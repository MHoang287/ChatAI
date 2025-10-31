# main.py
#
# FastAPI chatbot service
# Chạy: uvicorn main:app --host 0.0.0.0 --port 9000 --reload
# API chính:
#   POST /api/ask { "question": "..." }
# trả về:
#   { "answer": "...", "matched_question": "...", "score": 2 }

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from knowledge_base import find_best_answer

app = FastAPI(title="AI Chatbot Service", version="1.0.0")

# Cho phép ASP.NET MVC (https://localhost:5001) và ngrok truy cập
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # dev mode: mở hết
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    matched_question: str | None = None
    score: int

@app.post("/api/ask", response_model=AskResponse)
def ask_chatbot(payload: AskRequest):
    result = find_best_answer(payload.question)
    return AskResponse(
        answer=result["answer"],
        matched_question=result["matched_question"],
        score=result["score"],
    )

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "chatbot"}
