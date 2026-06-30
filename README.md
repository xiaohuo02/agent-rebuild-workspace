# Agent Rebuild Workspace

这是一个从 0 重实现电商智能客服 Agent（智能体）的学习工作区。

它不修改原项目 `code/deepseek_agent`，而是用更小、更清晰的结构复刻核心设计：FastAPI（Python 后端框架）接入、ChatGPT 风格前端、Agentic Workflow（智能体工作流）、工具调用、Evidence（证据链）、测试与 DeepEval（大模型评测框架）骨架。

## 第一阶段目标

第一阶段只做 MVP（最小可行产品）：

1. 后端提供 `/health`、`/api/chat`、`/api/agent/query`。
2. 前端提供 ChatGPT 风格对话工作台。
3. Agent 链路包含 Router（路由器）、Guardrails（安全护栏）、Planner（规划器）、Tool Selection（工具选择）、Tool Execution（工具执行）、Final Answer（最终回答）。
4. 工具暂时使用 fake data（假数据），先跑通架构，再替换为 Neo4j、Text2Cypher 和 GraphRAG。
5. 所有工具结果都返回 Evidence（证据链），为幻觉检测和 DeepEval 评测做准备。

## 工作区结构

```text
agent-rebuild-workspace/
  docs/       学习文档、架构说明、面试讲法
  backend/    FastAPI + Agentic Workflow 后端
  frontend/   ChatGPT 风格对话前端
```

## 环境变量

后端环境变量模板在 `backend/.env.example`。复制成 `backend/.env` 后填写真实配置：

```powershell
Copy-Item backend\.env.example backend\.env
```

`backend/.env` 不会提交到 GitHub，真实 API Key（接口密钥）、数据库地址和模型配置都写在这里。

## 学习方式

每个模块按四个问题学习：

1. 它解决什么业务痛点？
2. 为什么要这样设计？
3. 代码如何实现？
4. 面试时怎么讲？

## 面试总讲法

> 我没有一开始复制完整生产系统，而是从 0 搭了一个可解释的 MVP。先用假数据跑通 Agentic Workflow（智能体工作流）：入口、路由、护栏、规划、工具选择、证据链和最终回答。这样能先证明架构成立，再逐步把假工具替换成 Neo4j、Text2Cypher 和 GraphRAG。前端采用 ChatGPT 风格对话工作台，右侧展示 Agent 过程和证据链，方便演示和解释系统内部链路。

## 启动方式

后端：

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8010
```

如果不想激活环境，也可以直接使用虚拟环境里的 Python：

```bash
cd backend
.\.venv\Scripts\python -m pip install -e ".[dev]"
.\.venv\Scripts\python -m pytest
.\.venv\Scripts\python -m uvicorn app.main:app --reload --port 8010
```

前端：

```bash
cd frontend
npm install
npm run dev
```

第一版后端不依赖真实数据库和真实大模型，可以直接用 fake data（假数据）验证主链路。

## CI/CD

当前已经配置 CI（持续集成），文件在 `.github/workflows/ci.yml`：

1. Backend tests（后端测试）：安装 `backend/pyproject.toml`，运行 `pytest`。
2. Frontend build（前端构建）：运行 `npm ci` 和 `npm run build`。

CD（持续部署）暂时不接，因为第一阶段还没有明确部署目标。等后续确定部署到服务器、Docker（容器）、Vercel（前端托管）或云平台后，再增加部署流水线。
