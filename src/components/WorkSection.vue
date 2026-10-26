<script setup>
import { work } from '../data.js'
import WorkCard from './WorkCard.vue'
</script>

<template>
  <section class="mt-16" aria-labelledby="work-heading">
    <h2 id="work-heading" class="font-display text-3xl tracking-tight sm:text-4xl">Work</h2>
    <ul class="mt-6 grid gap-4">
      <WorkCard v-for="item in work" :key="item.number" :item="item" />
    </ul>
  </section>
</template>
