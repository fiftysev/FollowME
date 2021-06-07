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
        <h3 class="text-xl self-center">{{title}}</h3>
        <!-- Здесь попытался подтянуть к рейтинг-компоненту значения из запроса, не получилось-->
        <rating :rating_value="rating"></rating>
      </div>
      <hr>
      <p>{{description}}</p>
      <hr>
      <div class="container flex">
        <!--Тут наверное немного костыльно, хотя это единственное, что работает из того, что пробовал-->
        <span
          v-for="tag in tags"
          v-bind:key="tag"
          :style="{background: tag.color}"
          class="m-4 p-2 rounded"
        >
          {{tag.tag}}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import Rating from '@/components/Rating'
export default {
  name: 'PlaceCard',
  components: { Rating },
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
