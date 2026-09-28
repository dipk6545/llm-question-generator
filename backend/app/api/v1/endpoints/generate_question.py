from fastapi import APIRouter
from app.services.llm_service import LLM_Service

router = APIRouter()
llm = LLM_Service()

@router.get("/generate")
async def generate_question(user_question: str = ""):
    question = await llm.generate_question(user_question)
    return {
        "question": question
    }