from app.agent.nodes.final_answer import build_final_answer
from app.agent.nodes.guardrails import apply_guardrails
from app.agent.nodes.planner import create_plan
from app.agent.nodes.tool_selection import execute_tools
from app.agent.router import route_query
from app.agent.state import AgentResponse, AgentState, TraceStep


async def run_agent(query: str, conversation_id: str | None = None) -> AgentResponse:
    state = AgentState(query=query, conversation_id=conversation_id)

    state.route = route_query(query)
    state.trace.append(
        TraceStep(name="router", status="done", detail=f"路由结果：{state.route}")
    )

    state = apply_guardrails(state)
    if state.route and state.route.value == "blocked":
        return build_final_answer(state)

    state = create_plan(state)
    state = execute_tools(state)
    return build_final_answer(state)
