from typing import Protocol


class ChatModel(Protocol):
    """Small interface that can later be backed by DeepSeek or Ollama."""

    async def complete(self, prompt: str) -> str:
        """Return a model completion for the prompt."""
