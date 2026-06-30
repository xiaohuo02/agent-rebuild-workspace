from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.agent.graph import run_agent
from app.agent.state import AgentRequest, AgentResponse
from app.core.config import settings
from app.llm.fake_llm import FakeChatModel

app = FastAPI(title=settings.app_name)
chat_model = FakeChatModel()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    answer = await chat_model.complete(request.message)
    return ChatResponse(answer=answer)


@app.post("/api/agent/query", response_model=AgentResponse)
async def agent_query(request: AgentRequest) -> AgentResponse:
    return await run_agent(request.query, request.conversation_id)
