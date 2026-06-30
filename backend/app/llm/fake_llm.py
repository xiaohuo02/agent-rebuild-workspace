from app.llm.base import ChatModel


class FakeChatModel(ChatModel):
    """Deterministic model for local learning and tests."""

    async def complete(self, prompt: str) -> str:
        return f"我已收到你的问题：{prompt}"
