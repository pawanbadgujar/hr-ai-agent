from fastapi import APIRouter

from app.services.ai_service import AIService

router = APIRouter(
    prefix="/chat",
    tags=["AI Chatbot"]
)


@router.post("/")
def chat(query: str):

    answer = AIService.ask(query)

    return {
        "question": query,
        "answer": answer
    }