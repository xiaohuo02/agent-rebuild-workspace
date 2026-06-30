from app.tools.policy_tool import query_policy
from app.tools.product_tool import query_product
from app.tools.schemas import ToolStatus


def test_product_tool_returns_evidence_for_known_product() -> None:
    result = query_product("智能门锁还有库存吗")

    assert result.status == ToolStatus.SUCCESS
    assert result.tool == "product_tool"
    assert result.evidence
    assert "智能门锁" in result.summary


def test_product_tool_returns_empty_for_unknown_product() -> None:
    result = query_product("空气炸锅还有库存吗")

    assert result.status == ToolStatus.EMPTY
    assert not result.evidence


def test_policy_tool_returns_evidence_for_policy() -> None:
    result = query_policy("智能门锁保修多久")

    assert result.status == ToolStatus.SUCCESS
    assert result.tool == "policy_tool"
    assert result.evidence
    assert "保修" in result.evidence[0].title


def test_policy_tool_returns_empty_for_unknown_policy() -> None:
    result = query_policy("会员积分怎么算")

    assert result.status == ToolStatus.EMPTY
    assert not result.evidence
