<template>
  <div
    class="grid min-h-screen place-items-center w-full"
  >
    <div
      class="w-11/12 p-12 bg-green-400 rounded-2xl sm:w-8/12 md:w-1/2 lg:w-5/12"
    >
      <h1
        class="text-xl font-semibold"
      > Введите данные для входа:
      </h1>
      <form
        class="mt-6"
      >
        <label
          for="username"
          class="block mt-2 text-xs font-semibold text-gray-600 uppercase"
        >Логин
        </label>
        <input
          v-model="username"
          id="username"
          type="text"
          name="username"
          placeholder="god_damn424"
          autocomplete="username"
          class="block w-full p-3 mt-2 text-gray-700 bg-gray-200 appearance-none focus:outline-none focus:bg-gray-300 focus:shadow-inner"
          required />
        <label
          for="password"
          class="block mt-2 text-xs font-semibold text-gray-600 uppercase"
        >Пароль
        </label>
        <input
          v-model="password"
          id="password"
          type="password"
          name="password"
          placeholder="********"
          autocomplete="new-password"
          class="block w-full p-3 mt-2 text-gray-700 bg-gray-200 appearance-none focus:outline-none focus:bg-gray-300 focus:shadow-inner"
          required />
        <button
          type="submit"
          class="w-full mt-5 py-2 tracking-widest uppercase font-medium bg-black rounded shadow-md hover:bg-blue-600 hover:shadow-none focus:outline-none"
          @click.prevent="handleLoginSubmit"
        ><span class="text-white">Войти</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  props: {
    nextUrl: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleLoginSubmit () {
      const username = this.username
      const password = this.password
      this.$store.dispatch('login', { username, password })
        .then(() => this.$router.push('/'))
        .catch(e => console.log(e))
    }
  }
}
</script>

<style scoped>
  input {
    @apply rounded-md
  }
  button {
    @apply rounded-lg
  }
</style>
