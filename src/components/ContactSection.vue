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
  <section class="mt-14" aria-labelledby="contact-heading">
    <h2 id="contact-heading" class="font-mono text-xs tracking-[0.22em] text-muted">CONTACT</h2>
    <p class="mt-3 flex flex-wrap items-baseline gap-x-4 gap-y-1 text-base">
      <a
        :href="`mailto:${profile.email}`"
        class="underline decoration-accent decoration-2 underline-offset-4"
      >
        {{ profile.email }}
      </a>
      <ExternalLink :href="profile.linkedin" class="text-accent">LinkedIn</ExternalLink>
    </p>
  </section>
</template>
