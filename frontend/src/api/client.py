import httpx
from src.core.config import BACKEND_URL

def fetch_question(user_question: str="") -> dict:
    try:
        response = httpx.get(
            f"{BACKEND_URL}/questions/generate",
            params = {"user_question" : user_question},
            timeout = 15.0
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return { "error" : str(e)}