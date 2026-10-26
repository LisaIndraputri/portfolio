<script setup>
import { experience } from '../data.js'
import { useActiveRole } from '../composables/useActiveRole.js'
import ExternalLink from './ExternalLink.vue'
import RoleItem from './RoleItem.vue'

const { show, isActive } = useActiveRole()
</script>

<template>
  <section class="mt-16" aria-labelledby="experience-heading">
    <div class="flex items-baseline justify-between gap-4">
      <div class="flex flex-wrap items-baseline gap-x-3 gap-y-1">
        <h2 id="experience-heading" class="font-display text-3xl tracking-tight sm:text-4xl">
          <ExternalLink
            :href="experience.href"
            class="underline decoration-accent/40 decoration-2 underline-offset-4 transition hover:decoration-accent"
          >
            {{ experience.company }}
            <span class="sr-only"> on Google Play</span>
          </ExternalLink>
        </h2>
        <ExternalLink :href="experience.appStore" class="font-mono text-xs text-accent">
          App Store
        </ExternalLink>
      </div>
      <p class="shrink-0 font-mono text-xs text-muted">{{ experience.range }}</p>
    </div>

    <ol class="mt-6 border-l border-line">
      <RoleItem
        v-for="role in experience.roles"
        :key="role.title"
        :role="role"
        :active="isActive(role.title)"
        @show="show(role.title)"
      />
    </ol>
  </section>
</template>
