from enum import StrEnum

from pydantic import BaseModel, Field

from app.tools.schemas import Evidence, ToolResult


class RouteType(StrEnum):
    GENERAL = "general"
    PRODUCT = "product"
    POLICY = "policy"
    MIXED = "mixed"
    BLOCKED = "blocked"


class PlanTask(BaseModel):
    id: str
    description: str
    expected_tool: str


class TraceStep(BaseModel):
    name: str
    status: str
    detail: str


class AgentRequest(BaseModel):
    query: str
    conversation_id: str | None = None


class AgentResponse(BaseModel):
    answer: str
    route: RouteType
    tasks: list[PlanTask] = Field(default_factory=list)
    tool_results: list[ToolResult] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    trace: list[TraceStep] = Field(default_factory=list)


class AgentState(BaseModel):
    query: str
    conversation_id: str | None = None
    route: RouteType | None = None
    tasks: list[PlanTask] = Field(default_factory=list)
    tool_results: list[ToolResult] = Field(default_factory=list)
    trace: list[TraceStep] = Field(default_factory=list)
