from app.tools.schemas import Evidence, ToolResult, ToolStatus


POLICIES = {
    "保修": "智能硬件自签收日起享受 1 年有限保修，非人为质量问题可申请售后检测。",
    "退货": "商品签收 7 天内，在不影响二次销售的情况下可申请无理由退货。",
    "换货": "商品签收 15 天内，如确认质量问题，可申请换货或维修。",
}


def query_policy(task: str) -> ToolResult:
    matched_key = next((key for key in POLICIES if key in task), None)
    if not matched_key:
        return ToolResult(
            tool="policy_tool",
            status=ToolStatus.EMPTY,
            summary="没有匹配到售后政策。",
        )

    content = POLICIES[matched_key]
    return ToolResult(
        tool="policy_tool",
        status=ToolStatus.SUCCESS,
        summary=content,
        evidence=[
            Evidence(
                source="fake_after_sales_policy",
                title=f"{matched_key}政策",
                content=content,
                metadata={"policy": matched_key},
            )
        ],
    )
