<template>
  <div class="place flex justify-center py-52">
    <h3>{{category}}</h3>
    <PlaceCard
      title="{{placeOptions.title}}"
      address="{{placeOptions.address}}"
      description="{{placeOptions.description}}"
      tags="{{placeOptions.tags}}}"
      bus_station="{{placeOptions.bus_station}}"
      image="{{placeOptions.image}}"
      rating="{{placeOptions.rating}}"
    />
  </div>
</template>

<script>
import PlaceCard from '@/components/PlaceCard'
export default {
  name: 'CardView',
  components: { PlaceCard },
  data() {
    return {
      loading: true,
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
  async mounted() {
    let response = await fetch(`/place/${this.props.category}`)
    this.placeOptions = await response.json()
  }
}
</script>

<style scoped>

</style>
