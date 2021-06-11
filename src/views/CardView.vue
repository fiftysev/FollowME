<template>
  <div class="w-4/5 place flex justify-center py-12">
    <PlaceCardSkeletonLoader
      v-if="loading"
    >
    </PlaceCardSkeletonLoader>
    <PlaceCard
      v-else
      :title="placeOptions.title"
      :address="placeOptions.address"
      :description="placeOptions.description"
      :tags="placeOptions.tags"
      :bus_station="placeOptions.bus_station"
      :photo="placeOptions.photo"
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
        photo: ''
      }
    }
  },
  async created () {
    this.loading = true
    this.placeOptions = await this.$store.getters.lastPlace
    this.loading = false
  }
}
</script>

<style scoped>

</style>
