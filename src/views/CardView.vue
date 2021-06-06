<template>
  <div class="place flex justify-center py-52">
    <h3 v-if="loading" class="text-black">Загружаю данные...</h3>
    <PlaceCard
      v-else
      :title="placeOptions.title"
      :address="placeOptions.address"
      :description="placeOptions.description"
      :tags="placeOptions.tags"
      :bus_station="placeOptions.bus_station"
      :image="placeOptions.image"
      :rating="placeOptions.rating"
    />
  </div>
</template>

<script>
import PlaceCard from '@/components/PlaceCard'
export default {
  name: 'CardView',
  components: { PlaceCard },
  data () {
    return {
      loading: false,
      placeOptions: {
        title: '',
        address: '',
        description: '',
        bus_station: '',
        rating: null,
        tags: [],
        image: ''
      }
    }
  },
  props: {
    category: {
      type: String,
      default: ''
    }
  },
  async created () {
    this.loading = true
    const response = await fetch(`/place/${this.category}`)
    this.placeOptions = await response.json()
    this.loading = false
  }
}
</script>

<style scoped>

</style>
