<template>
    <div class="app container--fluid main grid min-h-screen place-items-center">
      <div class="navbar">
        <h2 class="font-light text-white text-2xl">С Л Е Д У Й З А М Н О Й</h2>
      </div>
      <div class="container grid place-items-center min-h-screen">
        <router-view></router-view>
      </div>
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
    background-size: 100%;
  }
  .app {
    @apply flex flex-col items-center
  }
  .navbar {
    @apply flex justify-between bg-opacity-50
  }
</style>
