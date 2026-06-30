from app.agent.state import AgentState, TraceStep
from app.tools.policy_tool import query_policy
from app.tools.product_tool import query_product
from app.tools.schemas import ToolResult, ToolStatus


def execute_tools(state: AgentState) -> AgentState:
    results: list[ToolResult] = []
    for task in state.tasks:
        if task.expected_tool == "product_tool":
            results.append(query_product(task.description))
        elif task.expected_tool == "policy_tool":
            results.append(query_policy(task.description))
        else:
            results.append(
                ToolResult(
                    tool=task.expected_tool,
                    status=ToolStatus.FAILED,
                    summary="未知工具。",
                    error="unsupported_tool",
                )
            )

    state.tool_results = results
    state.trace.append(
        TraceStep(
            name="tool_selection",
            status="done",
            detail=f"执行 {len(results)} 个工具调用。",
        )
    )
    return state
