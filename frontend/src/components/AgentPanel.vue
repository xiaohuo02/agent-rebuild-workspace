<script setup lang="ts">
import type { Evidence, RouteType, TraceStep } from "../types/agent";

defineProps<{
  route?: RouteType;
  trace: TraceStep[];
  evidence: Evidence[];
}>();
</script>

<template>
  <aside class="agent-panel">
    <div class="panel-section">
      <p class="eyebrow">Agent route</p>
      <h2>{{ route || "waiting" }}</h2>
    </div>

    <div class="panel-section">
      <p class="section-label">过程</p>
      <ol class="trace-list" v-if="trace.length">
        <li v-for="step in trace" :key="`${step.name}-${step.detail}`">
          <span class="trace-dot" :class="step.status"></span>
          <div>
            <strong>{{ step.name }}</strong>
            <p>{{ step.detail }}</p>
          </div>
        </li>
      </ol>
      <p class="muted" v-else>等待提问</p>
    </div>

    <div class="panel-section">
      <p class="section-label">证据</p>
      <div v-if="evidence.length" class="evidence-list">
        <article v-for="item in evidence" :key="`${item.source}-${item.title}`" class="evidence-item">
          <strong>{{ item.title }}</strong>
          <p>{{ item.content }}</p>
          <span>{{ item.source }}</span>
        </article>
      </div>
      <p class="muted" v-else>暂无证据</p>
    </div>
  </aside>
</template>
