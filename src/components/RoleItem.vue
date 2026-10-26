<script setup>
defineProps({
  role: {
    type: Object,
    required: true,
  },
  active: {
    type: Boolean,
    required: true,
  },
})

defineEmits(['show'])
</script>

<template>
  <li>
    <div class="relative">
      <span
        class="absolute top-1/2 -left-[5px] size-2.5 -translate-y-1/2 rounded-full transition-all duration-300"
        :class="active ? 'scale-125 bg-accent shadow-[0_0_12px_var(--color-accent)]' : 'bg-line'"
      />
      <button
        type="button"
        class="flex w-full cursor-pointer items-baseline justify-between gap-4 rounded-md py-3 pr-2 pl-6 text-left transition duration-300"
        :class="active ? 'bg-panel text-ink' : 'text-muted hover:text-ink'"
        :aria-expanded="active"
        @mouseenter="$emit('show')"
        @focus="$emit('show')"
        @click="$emit('show')"
      >
        <span :class="active ? 'text-lg font-medium' : ''">{{ role.title }}</span>
        <span class="shrink-0 font-mono text-xs">{{ role.years }}</span>
      </button>
    </div>
    <div class="role-panel" :class="{ open: active }" :inert="!active">
      <div>
        <ul class="grid gap-1.5 py-3 pl-6 text-sm text-ink/90">
          <li v-for="detail in role.details" :key="detail">{{ detail }}</li>
        </ul>
      </div>
    </div>
  </li>
</template>

<style scoped>
.role-panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.35s ease;
}

.role-panel.open {
  grid-template-rows: 1fr;
}

.role-panel > div {
  overflow: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .role-panel {
    transition: none;
  }
}
</style>
