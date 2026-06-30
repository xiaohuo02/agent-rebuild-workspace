<script setup lang="ts">
import type { ChatMessage } from "../types/agent";

defineProps<{
  message: ChatMessage;
}>();
</script>

<template>
  <article class="message" :class="message.role">
    <div class="message-avatar">{{ message.role === "user" ? "你" : "AI" }}</div>
    <div class="message-body">
      <p>{{ message.content }}</p>
      <span v-if="message.status === 'sending'" class="message-state">生成中</span>
      <span v-if="message.status === 'failed'" class="message-state failed">发送失败</span>
    </div>
  </article>
</template>
