from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Honeypot-AI")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HONEYPOT_API_KEY: str = os.getenv("HONEYPOT_API_KEY")

    if not HONEYPOT_API_KEY:
        raise ValueError("HONEYPOT_API_KEY is missing in .env file")

settings = Settings()
