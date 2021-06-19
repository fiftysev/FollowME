<template>
    <v-rating
      v-model="userRating"
      half-increments
      hover
      length="5"
      :size="starSize"
      color="#ffd061"
      background-color="#ffdc8a"
    ></v-rating>
</template>

<script>
export default {
  name: 'rating',
  data () {
    return {
      userRating: null
    }
  },

  computed: {
    starSize () {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return 24
        case 'sm': return 24
        case 'md': return 32
        case 'lg': return 32
        case 'xl': return 32
        default: return 48
      }
    }
  },
  methods: {
  }
}

</script>

<style scoped>

</style>
