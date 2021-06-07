<template>
  <div class="container shadow-md flex bg-white rounded justify-between">
    <div class="w-1/3 p-8 flex flex-col text-center">
        <v-skeleton-loader
          class="rounded-2xl"
          type="image"
        ></v-skeleton-loader>

      <v-skeleton-loader type="list-item" class="py-4"></v-skeleton-loader>
      <hr>
      <v-skeleton-loader type="list-item" class="py-4"></v-skeleton-loader>
      <hr>
    </div>

    <div class="w-2/3 flex flex-col justify-around p-8 text-left">
      <v-skeleton-loader type="list-item" class="text-xl"></v-skeleton-loader>
      <hr>
      <v-skeleton-loader type="paragraph"></v-skeleton-loader>
      <hr>
      <v-skeleton-loader type="list-item"></v-skeleton-loader>
    </div>
  </div>

</template>

<script>
export default {
  name: 'PlaceCardSkeletonLoader'
}
</script>

<style scoped>

</style>
