<script setup>
import { skills, skillsIntro } from '../data.js'
</script>

<template>
  <section class="mt-12" aria-labelledby="skills-heading">
    <h2 id="skills-heading" class="font-mono text-xs tracking-[0.22em] text-accent">SKILLS</h2>
    <p class="mt-4 max-w-md leading-relaxed text-ink/90">{{ skillsIntro }}</p>
    <ul class="mt-5 flex flex-wrap gap-2">
      <li
        v-for="skill in skills"
        :key="skill"
        class="border border-line bg-panel/70 px-3 py-1 font-mono text-xs text-muted transition hover:border-accent/70 hover:text-accent"
      >
        {{ skill }}
      </li>
    </ul>
  </section>
</template>
