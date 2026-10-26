<script setup>
import { profile } from './data.js'
import ContactSection from './components/ContactSection.vue'
import ExperienceSection from './components/ExperienceSection.vue'
import HeroSection from './components/HeroSection.vue'
import SiteHeader from './components/SiteHeader.vue'
import SkillsSection from './components/SkillsSection.vue'
import WorkSection from './components/WorkSection.vue'
</script>

<template>
  <div class="relative min-h-screen text-ink">
    <SiteHeader :profile="profile" />
    <main id="top" class="mx-auto max-w-3xl px-5 pb-24 sm:px-8">
      <HeroSection :profile="profile" />
      <ExperienceSection />
      <SkillsSection />
      <WorkSection />
      <ContactSection :profile="profile" />
    </main>
  </div>
</template>
