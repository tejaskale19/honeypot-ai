import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Honeypot-AI")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HONEYPOT_API_KEY: str = os.getenv("HONEYPOT_API_KEY", "guvi-demo-key-123")

settings = Settings()

