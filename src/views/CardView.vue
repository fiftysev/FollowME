<template>
  <div class=" w-2/3 place flex justify-center py-12">
    <PlaceCardSkeletonLoader
      v-if="loading"
      class="w-2/3 rounded-md">
    </PlaceCardSkeletonLoader>
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
import PlaceCardSkeletonLoader from '@/components/PlaceCardSkeletonLoader'
export default {
  name: 'CardView',
  components: { PlaceCard, PlaceCardSkeletonLoader },
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
