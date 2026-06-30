import type { AgentResponse } from "../types/agent";

const API_BASE = "";

export async function askAgent(query: string, conversationId: string): Promise<AgentResponse> {
  const response = await fetch(`${API_BASE}/api/agent/query`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      query,
      conversation_id: conversationId
    })
  });

  if (!response.ok) {
    throw new Error(`请求失败：${response.status}`);
  }

  return response.json();
}
