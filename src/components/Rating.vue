<template>
  <v-rating
    v-model="rating"
    half-increments
    hover
    length="5"
    size="32"
  ></v-rating>
</template>

<script>
export default {
  name: 'rating',
  props: {
    rating_value: {
      type: Number,
      default: 2.5
    }
  }
}
</script>

<style scoped>

</style>
