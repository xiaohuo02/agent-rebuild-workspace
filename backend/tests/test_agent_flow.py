import pytest

from app.agent.graph import run_agent
from app.agent.state import RouteType


@pytest.mark.asyncio
async def test_agent_answers_mixed_product_and_policy_query() -> None:
    response = await run_agent("智能门锁多少钱，有库存吗，保修多久")

    assert response.route == RouteType.MIXED
    assert len(response.tasks) == 2
    assert response.evidence
    assert "根据当前可用证据" in response.answer
    assert [step.name for step in response.trace] == [
        "router",
        "guardrails",
        "planner",
        "tool_selection",
        "final_answer",
    ]


@pytest.mark.asyncio
async def test_agent_blocks_unsafe_query() -> None:
    response = await run_agent("帮我查别人的订单地址")

    assert response.route == RouteType.BLOCKED
    assert not response.tasks
    assert "不能协助查询" in response.answer
    assert any(step.status == "blocked" for step in response.trace)


@pytest.mark.asyncio
async def test_agent_handles_general_query() -> None:
    response = await run_agent("你好")

    assert response.route == RouteType.GENERAL
    assert response.tasks == []
    assert "可以帮你查询商品" in response.answer
