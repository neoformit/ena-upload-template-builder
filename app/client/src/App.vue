<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Landing from './components/Landing.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Intro</RouterLink>
        <RouterLink to="/form-1">Form 1</RouterLink>
        <RouterLink to="/form-2">Form 2</RouterLink>
        <RouterLink to="/submit">Submit</RouterLink>
      </nav>

      <Landing />
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
