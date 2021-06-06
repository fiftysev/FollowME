<template>
    <div class="app container--fluid main">
      <div class="navbar mb-44">
        <h2 class="font-bold text-white text-2xl">С Л Е Д У Й З А М Н О Й</h2>
      </div>
      <router-view></router-view>
    </div>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  })
}
</script>

<style scoped>
  .main {
    background: url('./assets/sora-sagano-Br9RTmdSeTo-unsplash.jpg');
    background-size: cover;
    height: 100vh;
  }
  .app {
    @apply flex flex-col items-center
  }
  .navbar {
    @apply flex justify-between bg-opacity-50
  }
</style>
