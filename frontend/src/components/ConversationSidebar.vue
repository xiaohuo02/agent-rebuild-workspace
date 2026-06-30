<script setup lang="ts">
import type { Conversation } from "../types/agent";

defineProps<{
  conversations: Conversation[];
  activeId: string;
}>();

const emit = defineEmits<{
  select: [id: string];
  create: [];
}>();
</script>

<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <div>
        <p class="eyebrow">AssistGen</p>
        <h1>智能客服</h1>
      </div>
      <button class="icon-button" type="button" title="新对话" @click="emit('create')">+</button>
    </div>

    <div class="conversation-list" v-if="conversations.length">
      <button
        v-for="conversation in conversations"
        :key="conversation.id"
        class="conversation-item"
        :class="{ active: conversation.id === activeId }"
        type="button"
        @click="emit('select', conversation.id)"
      >
        <span class="conversation-title">{{ conversation.title }}</span>
        <span class="conversation-summary">{{ conversation.summary }}</span>
        <span class="conversation-status">{{ conversation.status }}</span>
      </button>
    </div>

    <div class="empty-list" v-else>暂无会话</div>
  </aside>
</template>
