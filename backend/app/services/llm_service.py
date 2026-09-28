import json
from pathlib import Path
from openai import OpenAI
from app.core.config import LLMConfig

class LLM_Service:
    def __init__(self):
        self.config = LLMConfig()
        self.provider, self.model, self.api_key, self.base_url = self.config.get_config()
        
        if not self.api_key:
            raise ValueError(f"API key missing for provider: {self.provider}")
            
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        self.prompts = self.load_prompt_json()

    def load_prompt_json(self) -> dict:
        # Resolves: backend/app/core/prompts.json
        prompt_path = Path(__file__).resolve().parent.parent / "core" / "prompts.json"
        with open(prompt_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def generate_question(self, user_question: str = "") -> str:
        q_gen = self.prompts.get("question_generation", {})
        system_content = q_gen.get("system", "You are an expert technical interviewer.")
        default_user = q_gen.get("user_template", "Generate a single interview question.")
        
        user_content = user_question if user_question else default_user

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
        )
        return response.choices[0].message.content




if __name__ == "__main__":
    service = LLM_Service()
    print(f"Provider: {service.provider}")
    print(f"Model: {service.model}")
    print("Testing response...")
    result = service.generate_question()
    print("\nResult:\n", result)