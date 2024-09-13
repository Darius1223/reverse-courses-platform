<template data-bs-theme="dark">
  <nav-bar></nav-bar>

  <main>
    <router-view></router-view>
  </main>
  <FooterBar></FooterBar>
</template>

<style lang="scss">
@import "./styles/main.scss";


main{
  min-height: 95vh
}
</style>

<script setup>
import FooterBar from "./components/FooterBar.vue";
import NavBar from "./components/NavBar.vue";
</script>
