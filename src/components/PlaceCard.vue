<template>
  <div class="container shadow-md flex justify-between">
    <img :src="image" alt="">
    <div class="container flex flex-col justify-between">
      <h3>{{title}}</h3>
      <p>{{description}}</p>
      <span>{{address}}</span>
      <span>{{bus_station}}</span>
      <h4>{{rating}}</h4>
      <span v-for="tag in tags" v-bind:key="tag" >{{tag}}</span>
    </div>
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
