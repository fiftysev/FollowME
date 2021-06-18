<template>
    <v-rating
      v-model="userRating"
      half-increments
      hover
      length="5"
      :size="starSize"
      @input="rate"
      color="#ffd061"
      background-color="#ffdc8a"
    ></v-rating>
<!-- Сделать вывод среднего рейтинга, прилетающего с сервера, компонент нужен только для отправки данных о рейтинге на сервер -->
</template>

<script>
export default {
  name: 'rating',
  props: {
    _id: {
      type: String,
      default: '1'
    }
  },

  data () {
    return {
      placeId: this._id,
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
    async rate () {
      await request('/generator/rate', {
        placeId: this.placeId,
        userRating: this.userRating
      })
    },

    test_rate () {
      console.log(this._id)
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
