"""Model client selector for local and cloud environments."""

from Personalized_Holiday_Management.config.settings import IS_RENDER, MODEL_PROVIDER
from Personalized_Holiday_Management.models.gpt_model import create_openai_client
from Personalized_Holiday_Management.models.ollama_model import create_ollama_client


def _resolve_provider() -> str:
    if MODEL_PROVIDER in {"ollama", "openai"}:
        return MODEL_PROVIDER
    if MODEL_PROVIDER != "auto":
        raise ValueError(
            "Invalid MODEL_PROVIDER. Use one of: auto, ollama, openai."
        )

    # Default behavior:
    # - local/dev -> ollama
    # - Render/cloud -> openai
    return "openai" if IS_RENDER else "ollama"


def create_model_client():
    provider = _resolve_provider()
    if provider == "openai":
        return create_openai_client()
    return create_ollama_client()


model_client = create_model_client()
