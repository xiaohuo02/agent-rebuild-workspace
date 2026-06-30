from app.agent.state import AgentState, PlanTask, RouteType, TraceStep


def create_plan(state: AgentState) -> AgentState:
    if state.route == RouteType.BLOCKED:
        return state

    if state.route == RouteType.GENERAL:
        state.tasks = []
    elif state.route == RouteType.PRODUCT:
        state.tasks = [
            PlanTask(
                id="task_product",
                description=state.query,
                expected_tool="product_tool",
            )
        ]
    elif state.route == RouteType.POLICY:
        state.tasks = [
            PlanTask(
                id="task_policy",
                description=state.query,
                expected_tool="policy_tool",
            )
        ]
    else:
        state.tasks = [
            PlanTask(
                id="task_product",
                description=state.query,
                expected_tool="product_tool",
            ),
            PlanTask(
                id="task_policy",
                description=state.query,
                expected_tool="policy_tool",
            ),
        ]

    state.trace.append(
        TraceStep(
            name="planner",
            status="done",
            detail=f"生成 {len(state.tasks)} 个子任务。",
        )
    )
    return state
