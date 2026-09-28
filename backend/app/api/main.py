from fastapi import FastAPI
from fastapi import APIRouter
from app.api.v1.router import api_router

def create_server() -> FastAPI:
    app = FastAPI(
        title="Interview AI API",
        description="LLM-powered interview question generation and evaluation service",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Mounts router under /api/v1
    app.include_router(api_router, prefix="/api/v1")

    @app.get('/')
    def health_check():
        return {
            "status" : "ok",
            "service" : "Intervew-Question-app",
            "version" : "1.0",
        }

    return app

app = create_server()



