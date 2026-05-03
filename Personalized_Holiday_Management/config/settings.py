import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma4:26b-a4b-it-q4_K_M")

# Values: auto | ollama | openai
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "auto").strip().lower()

# Render sets one or both of these.
IS_RENDER = (
    os.getenv("RENDER", "").strip().lower() == "true"
    or bool(os.getenv("RENDER_EXTERNAL_URL"))
)