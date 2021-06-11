<template>
    <div class="app container--fluid main grid min-h-screen place-items-center">
      <div class="navbar w-full min-h-navbar flex flex-col lg:flex-row pt-4 lg:px-32 items-center justify-between">
        <div class="flex flex-row">
          <h2 class="font-bold text-white text-xl md:text-3xl xl:text-4xl pr-2 lg:p-0">
            <router-link tag="a" :to="{name: 'Home'}">
              С Л Е Д У Й З А М Н О Й
            </router-link>
          </h2>
          <div class="button lg:hidden"
               @click="buttonsHidden = !buttonsHidden"
          >
            <v-icon
                 class="text-green-600 w-full h-full"
                 size="24"
                 style="color: mediumseagreen"
            >
              {{getArrowDirection}}
            </v-icon>
          </div>
        </div>
        <div class="buttons flex-col items-center lg:flex-row lg:flex"
             :class="{'hidden': buttonsHidden, 'flex': !buttonsHidden}">
            <div
              class="border-2 rounded-lg
                     px-3 py-2 mt-4 lg:my-0 lg:mr-3
                     hover:text-white font-bold
                     cursor-pointer
                     border-green-600 hover:bg-green-600 text-green-200
                    "
              @click="button1Handler"
            >
              <v-icon v-if="isAuth"
                      style="color: white"
              >
                mdi-account
              </v-icon>
              {{ getButton1Text }}
            </div>
          <div
            class="border-2  rounded-lg
                   px-3 py-2 mt-4 lg:m-0
                   hover:text-white font-bold
                   cursor-pointer
                  "
            :class="{
            'border-red-600 text-red-200 hover:bg-red-600': isAuth,
            'border-blue-600 text-blue-200 hover:bg-blue-600': !isAuth
            }"
            @click="button2Handler"
          >
            {{ getButton2Text }}
          </div>
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

  data () {
    return {
      buttonsHidden: true
    }
  },
  computed: {
    isAuth () {
      return this.$store.getters.isAuth
    },

    getButton1Text () {
      return this.isAuth ? 'Профиль' : 'Авторизация'
    },

    getButton2Text () {
      return this.isAuth ? 'Выйти' : 'Регистрация'
    },

    button1Handler () {
      return this.isAuth ? this.handleProfileTransition : this.handleLogin
    },

    button2Handler () {
      return this.isAuth ? this.handleLogout : this.handleSignup
    },

    getArrowDirection () {
      return this.buttonsHidden ? 'mdi-arrow-down-drop-circle-outline' : 'mdi-arrow-up-drop-circle-outline'
    }

  },
  methods: {
    handleLogout () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.go(-1)
        })
    },

    handleProfileTransition () {
      this.$router.push('/userboard')
    },

    handleLogin () {
      this.$router.push('/login')
    },

    handleSignup () {
      this.$router.push('/signup')
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
