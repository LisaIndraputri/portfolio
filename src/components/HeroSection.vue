<script setup>
defineProps({
  profile: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <section class="pt-14">
    <p class="font-mono text-xs tracking-[0.22em] text-accent">SOFTWARE ENGINEER</p>
    <h1 class="mt-4 font-display text-[clamp(3.1rem,10vw,6rem)] leading-[0.92] tracking-tight">
      {{ profile.name }}
    </h1>
    <p class="mt-6 max-w-md text-lg leading-snug text-ink/90 sm:text-xl">{{ profile.title }}</p>
    <p class="mt-2 font-mono text-sm text-muted">{{ profile.line }}</p>
  </section>
</template>
