<template>
  <div class="container shadow-md">

  </div>
</template>

<script>
export default {
  name: 'PlaceCard',
  props: {
    title: {
      type: String,
      default: 'ДВФУ'
    },
    image: {
      type: String,
      default: 'unsplash.com'
    },
    address: {
      type: String,
      default: 'Адрес'
    },
    description: {
      type: String,
      default: 'Описание'
    },
    bus_station: {
      type: String,
      default: 'Некрасовская, 50'
    },
    rating: {
      type: Number,
      default: 5.0
    },
    tags: {
      type: Array,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
