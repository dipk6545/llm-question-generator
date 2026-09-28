from fastapi import APIRouter
from app.services.llm_service import LLM_Service

router = APIRouter()
llm = LLM_Service()

@router.get("/generate")
def generate_question(user_question: str = ""):
    return {
        "question" : llm.generate_question(user_question)
    }