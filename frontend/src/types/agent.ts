export type RouteType = "general" | "product" | "policy" | "mixed" | "blocked";

export interface Evidence {
  source: string;
  title: string;
  content: string;
  metadata: Record<string, string>;
}

export interface PlanTask {
  id: string;
  description: string;
  expected_tool: string;
}

export interface ToolResult {
  tool: string;
  status: "SUCCESS" | "EMPTY" | "FAILED" | "BLOCKED";
  summary: string;
  evidence: Evidence[];
  error?: string | null;
}

export interface TraceStep {
  name: string;
  status: string;
  detail: string;
}

export interface AgentResponse {
  answer: string;
  route: RouteType;
  tasks: PlanTask[];
  tool_results: ToolResult[];
  evidence: Evidence[];
  trace: TraceStep[];
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  status?: "sending" | "done" | "failed";
}

export interface Conversation {
  id: string;
  title: string;
  summary: string;
  status: "处理中" | "已解决";
  messages: ChatMessage[];
  lastTrace: TraceStep[];
  lastEvidence: Evidence[];
  lastRoute?: RouteType;
}
