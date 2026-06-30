from app.agent.state import AgentState, RouteType, TraceStep


def apply_guardrails(state: AgentState) -> AgentState:
    if state.route == RouteType.BLOCKED:
        state.trace.append(
            TraceStep(
                name="guardrails",
                status="blocked",
                detail="问题涉及越权、隐私或系统规则，已拦截。",
            )
        )
        return state

    state.trace.append(
        TraceStep(name="guardrails", status="done", detail="未发现越权或违规风险。")
    )
    return state
