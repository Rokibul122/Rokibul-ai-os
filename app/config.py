import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Config:
    APP_NAME = os.getenv("APP_NAME", "ROKIBUL AI OS")
    APP_VERSION = os.getenv("APP_VERSION", "5.0.0")

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-key-change-before-deployment"
    )

    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", "5000"))

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR / 'rokibul_ai_os.db'}"
    )

    AI_PROVIDER = os.getenv("AI_PROVIDER", "demo")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "")

    JSON_SORT_KEYS = False
