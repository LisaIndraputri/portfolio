import { ref } from 'vue'
import { experience } from '../data.js'

const activeTitle = ref(experience.roles[0].title)

export function useActiveRole() {
  function show(title) {
    activeTitle.value = title
  }

  function isActive(title) {
    return activeTitle.value === title
  }

  return { activeTitle, show, isActive }
}
