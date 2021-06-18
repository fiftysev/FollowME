<template>
  <div class="container
              flex flex-col text-center
              bg-blue-300 shadow-md rounded-2xl
              sm:text-xl md:text-2xl lg:text-xl xl:text-xl 2xl:text-2xl text-white
              p-4
              ">
    <img src="https://www.placecage.com/256/256"
         alt=""
         class="rounded-2xl object-cover self-center"
    >
    <h1>{{ username }}</h1>
    <h1>{{ firstName }}</h1>
    <h1>{{ lastName }}</h1>
    <div class="container flex flex-col">
      <div v-for="place in userPlaces"
           v-bind:key="place._id"
        class="flex p-2"
      >
        <img :src="place.photo"
             alt=""
             class="object-cover rounded-md"
        >
        <h1>{{place.name}}
          <v-icon
            color="#ffd061"
            background-color="#ffdc8a"
            :size="24"
            class="pr-2"
          >
            mdi-star
          </v-icon>
        </h1>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthUserBoard',

  props: {
    firstName: {
      type: String,
      default: 'A'
    },
    lastName: {
      type: String,
      default: 'A'
    },
    username: {
      type: String,
      default: 'AAAAAAAA'
    },
    userPlaces: {
      type: Array,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
