<script setup>
import ExternalLink from './ExternalLink.vue'

defineProps({
  item: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <li
    class="group border border-line bg-panel/50 p-5 transition duration-300 hover:-translate-y-0.5 hover:border-accent/70 hover:shadow-[0_0_28px_rgba(62,224,255,0.12)]"
  >
    <p class="font-mono text-xs text-accent">{{ item.number }}</p>
    <h3 class="mt-2 font-display text-3xl tracking-tight sm:text-4xl">
      <ExternalLink :href="item.href" class="transition group-hover:text-accent">
        {{ item.title }}
      </ExternalLink>
    </h3>
    <p class="mt-3 text-muted">{{ item.line }}</p>
    <ul class="mt-3 grid gap-1 text-sm text-ink/90">
      <li v-for="detail in item.details" :key="detail">{{ detail }}</li>
    </ul>
    <p class="mt-4 font-mono text-xs text-muted">
      {{ item.stack }}
      <ExternalLink :href="item.href" class="ml-3 text-accent">Open</ExternalLink>
    </p>
  </li>
</template>
