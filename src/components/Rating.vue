<template>
    <v-rating
      v-model="userRating"
      half-increments
      hover
      length="5"
      :size="star_size"
      v-resize
      @click.prevent="rate"
    ></v-rating>
<!-- Сделать вывод среднего рейтинга, прилетающего с сервера, компонент нужен только для отправки данных о рейтинге на сервер -->
</template>

<script>
export default {
  name: 'rating',
  props: {
    rating_value: {
      type: Number,
      default: 2.5
    }
  },

  data () {
    return {
      userRating: null
    }
  },

  computed: {
    star_size () {
      switch (this.$vuetify.breakpoint.name) {
        case 'sm': return 32
        case 'md': return 32
        case 'lg': return 48
        case 'xl': return 48
        default: return 24
      }
    }
  },
  methods: {
    async rate () {
      await request('/api/place', this.userRating)
    }
  }
}

async function request (url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    body: JSON.stringify(data)
  })
  return await response.json()
}
</script>

<style scoped>

</style>
