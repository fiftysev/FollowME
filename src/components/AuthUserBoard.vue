<template>
  <div class="container w-full bg-blue-300">
    <h1 class="font-bold text-white text-center text-2xl uppercase">{{ username }}</h1>
  </div>
</template>

<script>
export default {
  name: 'AuthUserBoard',
  data () {
    return {
      username: ''
    }
  },
  mounted () {
    const userdata = localStorage.getItem('user')
    const res = JSON.parse(userdata)
    this.username = res.username
  }
}
</script>

<style scoped>

</style>
