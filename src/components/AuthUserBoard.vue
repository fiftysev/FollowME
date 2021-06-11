<template>
  <div class="container w-full bg-blue-300">
    <h1 class="font-bold text-white text-center text-2xl uppercase">{{ username }}</h1>
    <h1 class="font-bold text-white text-center text-2xl uppercase">{{ firstName }}</h1>
    <h1 class="font-bold text-white text-center text-2xl uppercase">{{ lastName }}</h1>
  </div>
</template>

<script>
export default {
  name: 'AuthUserBoard',
  data () {
    return {
      firstName: '',
      lastName: '',
      username: ''
    }
  },
  created () {
    const user = this.$store.getters.authedUser
    this.username = user.username
    this.firstName = user.firstname
    this.lastName = user.lastname
  }
}
</script>

<style scoped>

</style>
