from fastapi import APIRouter
from app.api.v1.endpoints import generate_question

api_router = APIRouter()
api_router.include_router(generate_question.router, prefix="/questions", tags=["Questions"])