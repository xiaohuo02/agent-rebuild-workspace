<script setup lang="ts">
import { computed, nextTick, ref } from "vue";
import AgentPanel from "./components/AgentPanel.vue";
import ChatMessage from "./components/ChatMessage.vue";
import ConversationSidebar from "./components/ConversationSidebar.vue";
import { askAgent } from "./services/api";
import type { ChatMessage as ChatMessageType, Conversation } from "./types/agent";

const seedConversation: Conversation = {
  id: "conversation-1",
  title: "商品与售后咨询",
  summary: "智能门锁库存和保修",
  status: "处理中",
  messages: [
    {
      id: "welcome",
      role: "assistant",
      content: "你好，我可以帮你查询商品、库存和售后政策。",
      status: "done"
    }
  ],
  lastTrace: [],
  lastEvidence: []
};

const conversations = ref<Conversation[]>([seedConversation]);
const activeId = ref(seedConversation.id);
const input = ref("");
const isSending = ref(false);
const errorMessage = ref("");
const messagesEnd = ref<HTMLElement | null>(null);

const activeConversation = computed(() => {
  return conversations.value.find((item) => item.id === activeId.value) || conversations.value[0];
});

function scrollToBottom() {
  nextTick(() => messagesEnd.value?.scrollIntoView({ behavior: "smooth" }));
}

function createConversation() {
  const id = `conversation-${Date.now()}`;
  conversations.value.unshift({
    id,
    title: "新对话",
    summary: "开始一个客服问题",
    status: "处理中",
    messages: [],
    lastTrace: [],
    lastEvidence: []
  });
  activeId.value = id;
}

function selectConversation(id: string) {
  activeId.value = id;
  errorMessage.value = "";
  scrollToBottom();
}

async function submitQuestion() {
  const query = input.value.trim();
  if (!query || isSending.value) return;

  const conversation = activeConversation.value;
  const userMessage: ChatMessageType = {
    id: `user-${Date.now()}`,
    role: "user",
    content: query,
    status: "done"
  };
  const assistantMessage: ChatMessageType = {
    id: `assistant-${Date.now()}`,
    role: "assistant",
    content: "正在分析问题...",
    status: "sending"
  };

  conversation.messages.push(userMessage, assistantMessage);
  conversation.summary = query;
  input.value = "";
  isSending.value = true;
  errorMessage.value = "";
  scrollToBottom();

  try {
    const response = await askAgent(query, conversation.id);
    assistantMessage.content = response.answer;
    assistantMessage.status = "done";
    conversation.lastTrace = response.trace;
    conversation.lastEvidence = response.evidence;
    conversation.lastRoute = response.route;
    conversation.status = response.route === "blocked" ? "已解决" : "处理中";
  } catch (error) {
    assistantMessage.content = "请求失败，请确认后端服务已启动。";
    assistantMessage.status = "failed";
    errorMessage.value = error instanceof Error ? error.message : "未知错误";
  } finally {
    isSending.value = false;
    scrollToBottom();
  }
}
</script>

<template>
  <main class="workspace">
    <ConversationSidebar
      :conversations="conversations"
      :active-id="activeConversation.id"
      @create="createConversation"
      @select="selectConversation"
    />

    <section class="chat-shell">
      <header class="chat-header">
        <div>
          <p class="eyebrow">Customer conversation</p>
          <h2>{{ activeConversation.title }}</h2>
        </div>
        <span class="route-pill">{{ activeConversation.lastRoute || "ready" }}</span>
      </header>

      <div class="chat-messages">
        <div v-if="!activeConversation.messages.length" class="empty-chat">
          请选择一个问题开始测试。
        </div>
        <ChatMessage
          v-for="message in activeConversation.messages"
          :key="message.id"
          :message="message"
        />
        <div ref="messagesEnd"></div>
      </div>

      <p v-if="errorMessage" class="error-line">{{ errorMessage }}</p>

      <form class="composer" @submit.prevent="submitQuestion">
        <textarea
          v-model="input"
          rows="1"
          placeholder="问商品、库存或售后政策"
          @keydown.enter.exact.prevent="submitQuestion"
        ></textarea>
        <button type="submit" :disabled="!input.trim() || isSending">
          {{ isSending ? "发送中" : "发送" }}
        </button>
      </form>
    </section>

    <AgentPanel
      :route="activeConversation.lastRoute"
      :trace="activeConversation.lastTrace"
      :evidence="activeConversation.lastEvidence"
    />
  </main>
</template>
