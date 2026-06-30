from app.agent.state import AgentResponse, AgentState, RouteType, TraceStep
from app.tools.schemas import ToolStatus


def build_final_answer(state: AgentState) -> AgentResponse:
    evidence = [
        item
        for result in state.tool_results
        for item in result.evidence
        if result.status == ToolStatus.SUCCESS
    ]

    if state.route == RouteType.BLOCKED:
        answer = "这个问题涉及隐私或越权信息，我不能协助查询。"
    elif state.route == RouteType.GENERAL:
        answer = "你好，我可以帮你查询商品、库存、售后政策和使用说明。"
    elif evidence:
        summaries = "；".join(result.summary for result in state.tool_results)
        answer = f"根据当前可用证据：{summaries}"
    else:
        answer = "我暂时没有查到足够证据，建议补充商品名称或转人工处理。"

    state.trace.append(
        TraceStep(name="final_answer", status="done", detail="已生成最终回答。")
    )

    return AgentResponse(
        answer=answer,
        route=state.route or RouteType.GENERAL,
        tasks=state.tasks,
        tool_results=state.tool_results,
        evidence=evidence,
        trace=state.trace,
    )
