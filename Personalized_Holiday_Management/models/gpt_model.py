from autogen_ext.models.openai import OpenAIChatCompletionClient
from Personalized_Holiday_Management.config.settings import OPENAI_API_KEY, MODEL_NAME


def create_openai_client() -> OpenAIChatCompletionClient:
    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not set. Add it to your environment for OpenAI cloud usage."
        )

    return OpenAIChatCompletionClient(
        openai_api_key=OPENAI_API_KEY,
        model=MODEL_NAME,
    )
