<script setup>
import ExternalLink from './ExternalLink.vue'

defineProps({
  profile: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <header class="sticky top-0 z-10 border-b border-line/80 bg-void/70 backdrop-blur-md">
    <div class="mx-auto flex max-w-3xl items-center justify-between px-5 py-4 sm:px-8">
      <a href="#top" class="font-mono text-xs tracking-[0.18em] text-accent">LI</a>
      <span class="flex items-center gap-5 font-mono text-xs tracking-wide">
        <ExternalLink :href="profile.linkedin" class="text-muted transition hover:text-accent">
          LinkedIn
        </ExternalLink>
        <a :href="`mailto:${profile.email}`" class="text-muted transition hover:text-accent">
          Contact
        </a>
      </span>
    </div>
  </header>
</template>
