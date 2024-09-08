<template>
  <nav-bar></nav-bar>

  <main class="">
    <router-view></router-view>
  </main>
  <FooterBar></FooterBar>
</template>

<style lang="scss"></style>

<script setup>
import FooterBar from "./components/FooterBar.vue";
import NavBar from "./components/NavBar.vue";
</script>
