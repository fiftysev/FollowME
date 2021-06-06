<template>
  <div class="place flex justify-center py-52">
    <h3>{{category}}</h3>
    <PlaceCard/>
  </div>
</template>

<script>
import PlaceCard from '@/components/PlaceCard'
export default {
  name: 'CardView',
  components: { PlaceCard },
  props: {
    category: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>

</style>
