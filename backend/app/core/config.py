import os
import json
from pathlib import Path
from dotenv import load_dotenv

class LLMConfig:
    def __init__(self):
        load_dotenv()
        self.provider_config = self._load_providers()
        
        self.provider = os.getenv("LLM_PROVIDER", "groq").lower()
        provider_data = self.provider_config.get(self.provider, {})

        self.model = os.getenv("LLM_MODEL", provider_data.get("default_model", ""))
        self.base_url = provider_data.get("base_url")
        self.api_key = os.getenv(f"{self.provider.upper()}_API_KEY")

    def _load_providers(self) -> dict:
        config_path = Path(__file__).parent / "providers.json"
        with open(config_path, "r") as f:
            return json.load(f)

    def get_config(self):
        return self.provider, self.model, self.api_key, self.base_url