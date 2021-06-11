<template>
  <div class="container
              py-4 px-2 lg:p-0
              shadow-md
              flex flex-col lg:flex-row justify-between
              bg-white
              rounded-2xl sm:text-center
              sm:text-xl md:text-2xl lg:text-xl xl:text-xl 2xl:text-2xl">

    <div class="lg:w-1/2 pt-4 lg:p-8 flex flex-col justify-around text-center">
      <img
          :src="photo"
          alt=""
          class="rounded-2xl object-cover self-center
                  w-11/12"
      >
      <h3 class="text-2xl md:text-3xl self-center lg:hidden py-4">{{title}}</h3>
      <hr class="lg:hidden">
      <span class="py-4">{{address}}</span>
      <hr>
      <span class="py-4">{{bus_station}}</span>
      <hr>
    </div>

    <div class="lg:w-1/2 flex flex-col justify-around lg:p-8 text-center lg:text-left">
      <div class="container lg:flex lg:justify-between">

        <h3 class="lg:text-4xl xl:text-5xl 2xl:text-5xl
                   self-center
                   hidden lg:inline-block"
        >{{title}}</h3>

        <!-- Здесь попытался подтянуть к рейтинг-компоненту значения из запроса, не получилось-->
        <rating
          :rating_value="rating"
          class="self-center py-4 lg:p-0 lg:scale-200"
        ></rating>

      </div>
      <hr>
      <p class="py-4 lg:p-0 w-2/3 lg:w-full self-center lg:self-start">{{description}}</p>
      <hr>
      <div class="container flex py-4 lg:p-0 justify-center lg:justify-start">
        <!--Тут наверное немного костыльно, хотя это единственное, что работает из того, что пробовал-->
        <span
          v-for="tag in tags"
          v-bind:key="tag"
          class="m-4 py-3 px-4 w-24 sm:w-36 text-center rounded-full bg-green-300 capitalize"
        >
          {{tag}}
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
    photo: {
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
