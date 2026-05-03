from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core.models import ModelFamily
from Personalized_Holiday_Management.config.settings import OLLAMA_BASE_URL, OLLAMA_MODEL

def create_ollama_client() -> OllamaChatCompletionClient:
    return OllamaChatCompletionClient(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": True,
            "family": ModelFamily.UNKNOWN,
            "structured_output": True,
        },
    )
