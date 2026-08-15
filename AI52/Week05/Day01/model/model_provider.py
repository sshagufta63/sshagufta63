from ollama import OllamaProvider

def get_provider(provider_name: str, model_name: str):

    if provider_name == "ollama":
        return OllamaProvider(model_name)

    raise ValueError(f"Unsupported AI provider: {provider_name}")