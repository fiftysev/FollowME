<template>
    <div class="app container--fluid main grid min-h-screen place-items-center">
      <div class="navbar w-full min-h-navbar pt-4 px-32">
        <h2 class="font-bold text-white text-2xl md:text-3xl xl:text-4xl">
          <router-link tag="a" :to="{name: 'Home'}">
            С Л Е Д У Й З А М Н О Й
          </router-link>
        </h2>
        <div class="buttons flex" v-if="isAuth">
          <router-link tag="a" :to="{name: 'UserBoard'}">
            <div
              class="border-2 border-green-600 rounded-lg px-3 py-2 text-green-200 cursor-pointer hover:bg-green-600 hover:text-white font-bold mr-3"
            >
              <v-icon style="color: white">mdi-account</v-icon> Профиль
            </div>
          </router-link>
          <div
            class="border-2 border-red-600 rounded-lg px-3 py-2 text-red-200 cursor-pointer hover:bg-red-600 hover:text-white font-bold"
            @click="handleLogout"
          >
            Выйти
          </div>
        </div>
        <div class="buttons flex" v-else>
          <router-link tag="a" :to="{name: 'LogIn'}">
            <div
              class="border-2 border-green-600 rounded-lg px-3 py-2 text-green-200 cursor-pointer hover:bg-green-600 hover:text-white font-bold mr-3"
            >
              Авторизация
            </div>
          </router-link>
          <router-link tag="a" :to="{name: 'SignUp'}">
            <div
              class="border-2 border-blue-600 rounded-lg px-3 py-2 text-blue-200 cursor-pointer hover:bg-blue-600 hover:text-white font-bold"
            >
              Регистрация
            </div>
          </router-link>
        </div>
      </div>
      <div class="w-screen grid place-items-center min-h-main">
        <router-view></router-view>
      </div>
    </div>
</template>

<script>

export default {
  name: 'App',
  computed: {
    isAuth () {
      return this.$store.getters.isAuth
    }
  },
  methods: {
    handleLogout () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.go(-1)
        })
    }
  },
  created () {
    this.$http.interceptors.response.use(undefined, err => {
      return new Promise((resolve, reject) => {
        if (err.status === 401 && err.config) {
          this.$store.dispatch('logout')
        }
        throw err
      })
    })
  }
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
