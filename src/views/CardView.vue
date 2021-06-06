<template>
  <div class="place flex justify-center py-52">
    <semipolar-spinner
      v-if="loading"
      :animation-duration="2000"
      :size="130"
      :color="'#65dc9d'"
    />
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
import { SemipolarSpinner } from 'epic-spinners'
export default {
  name: 'CardView',
  components: { PlaceCard, SemipolarSpinner },
  data () {
    return {
      loading: true,
      placeOptions: {
        title: 'bar',
        address: 'bar',
        description: 'bar',
        bus_station: 'bar',
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
