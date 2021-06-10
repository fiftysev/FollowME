<template>
    <div class="app container--fluid main grid min-h-screen place-items-center">
      <div class="navbar min-h-navbar pt-4">
        <h2 class="font-bold text-white text-2xl md:text-3xl xl:text-4xl">
          <router-link tag="a" :to="{name: 'Home'}">
            С Л Е Д У Й З А М Н О Й
          </router-link>
        </h2>
      </div>
      <div class="w-screen grid place-items-center min-h-main">
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
    background-size: cover;
  }
  .app {
    @apply flex flex-col items-center
  }
  .navbar {
    @apply flex justify-between bg-opacity-50
  }
</style>
