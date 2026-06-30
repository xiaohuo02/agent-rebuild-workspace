# 02-MVP 实现计划

> For agentic workers: REQUIRED SUB-SKILL: Use subagent-driven-development or executing-plans when this plan is implemented task-by-task.

## Goal

实现一个可演示、可测试、可面试讲清楚的智能客服 Agent（智能体）MVP（最小可行产品）。

## Architecture

后端用 FastAPI 提供接口，用确定性 Python 节点模拟 Agentic Workflow（智能体工作流）。前端用 Vue 3 + Vite 构建 ChatGPT 风格对话工作台。工具先使用 fake data（假数据），通过统一 Evidence（证据链）结构约束最终回答。

## Tech Stack

Python、FastAPI、Pydantic、pytest、Vue 3、Vite、TypeScript。

## Global Constraints

1. 不修改原项目 `code/deepseek_agent`。
2. 第一阶段不依赖真实数据库、真实大模型和真实 GraphRAG。
3. 所有工具输出必须结构化。
4. 每个模块要能解释设计动机和面试讲法。

---

## Task 1: Backend API Skeleton

**Files:**

- `backend/app/main.py`
- `backend/app/core/config.py`
- `backend/requirements.txt`

**Interfaces:**

- `GET /health`
- `POST /api/chat`
- `POST /api/agent/query`

**Steps:**

1. 创建 FastAPI 应用。
2. 增加健康检查。
3. 增加普通聊天接口。
4. 增加 Agent 查询接口。
5. 用 pytest 验证接口存在。

## Task 2: Agent Workflow

**Files:**

- `backend/app/agent/state.py`
- `backend/app/agent/router.py`
- `backend/app/agent/graph.py`
- `backend/app/agent/nodes/*.py`

**Interfaces:**

- `run_agent(query: str, conversation_id: str | None) -> AgentResponse`

**Steps:**

1. 定义 Agent 状态和响应结构。
2. 实现 Router（路由器）。
3. 实现 Guardrails（安全护栏）。
4. 实现 Planner（规划器）。
5. 实现 Tool Selection（工具选择）。
6. 汇总工具结果并生成最终回答。

## Task 3: Tools and Evidence

**Files:**

- `backend/app/tools/schemas.py`
- `backend/app/tools/product_tool.py`
- `backend/app/tools/policy_tool.py`

**Interfaces:**

- `ToolResult`
- `Evidence`
- `query_product(task: str) -> ToolResult`
- `query_policy(task: str) -> ToolResult`

**Steps:**

1. 定义统一工具返回结构。
2. 实现商品库存假工具。
3. 实现售后政策假工具。
4. 工具失败时返回 `FAILED`，空结果返回 `EMPTY`。

## Task 4: Frontend Chat Workspace

**Files:**

- `frontend/src/App.vue`
- `frontend/src/services/api.ts`
- `frontend/src/types/agent.ts`
- `frontend/src/components/*.vue`

**Interfaces:**

- 调用 `POST /api/agent/query`
- 展示 answer、trace、evidence

**Steps:**

1. 搭建 Vue 3 + Vite。
2. 创建左侧会话栏。
3. 创建中央消息流。
4. 创建底部输入框。
5. 创建右侧 Agent 过程面板。

## Task 5: Tests and Eval Skeleton

**Files:**

- `backend/tests/test_router.py`
- `backend/tests/test_tools.py`
- `backend/tests/test_agent_flow.py`
- `backend/evals/datasets/router_cases.jsonl`
- `backend/evals/README.md`

**Steps:**

1. 测 Router 分类。
2. 测工具返回结构。
3. 测完整 Agent 流程。
4. 准备 DeepEval（大模型评测框架）数据集骨架。

## Self Review

1. 覆盖范围：后端、前端、测试、评测、文档都在计划内。
2. 第一阶段不依赖外部服务，适合学习和演示。
3. 后续可以逐步替换 fake tool（假工具）为真实 Neo4j、Text2Cypher 和 GraphRAG。
