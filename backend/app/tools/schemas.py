from enum import StrEnum

from pydantic import BaseModel, Field


class ToolStatus(StrEnum):
    SUCCESS = "SUCCESS"
    EMPTY = "EMPTY"
    FAILED = "FAILED"
    BLOCKED = "BLOCKED"


class Evidence(BaseModel):
    source: str
    title: str
    content: str
    metadata: dict[str, str] = Field(default_factory=dict)


class ToolResult(BaseModel):
    tool: str
    status: ToolStatus
    summary: str
    evidence: list[Evidence] = Field(default_factory=list)
    error: str | None = None
