<template>
  <div class="container shadow-md flex bg-white rounded justify-between">
    <div class="w-1/3 p-8 flex flex-col text-center">
      <div class="container pb-full overflow-hidden relative mb-4">
        <img :src="image" alt="" class="rounded-2xl absolute h-full w-full object-cover">
      </div>

      <span class="py-4">{{address}}</span>
      <hr>
      <span class="py-4">{{bus_station}}</span>
      <hr>
    </div>

    <div class="w-2/3 flex flex-col justify-around p-8 text-left">
      <div class="container flex justify-between">
        <h3 class="text-xl">{{title}}</h3>
        <h4>{{rating}}</h4>
      </div>
      <hr>
      <p>{{description}}</p>
      <hr>
      <div class="container flex">
        <span v-for="tag in tags" v-bind:key="tag" class="p-1">{{tag}}</span>
      </div>
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
