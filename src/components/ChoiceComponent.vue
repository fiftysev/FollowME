<template>
  <div class="card w-1/4 bg-green-400 py-5 rounded-md">
    <select
      name="placepicker"
      id="place"
      v-model="selected"
      class="w-11/12 bg-white opacity-30"
    >
      <option
        v-bind:value="option.value"
        v-for="option in options"
        :key="option.id"
      >
        {{option.text}}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  data () {
    return {
      selected: null,
      options: [
        { id: 1, value: 'bar', text: 'Бары' }
      ]
    }
  },
  async mounted () {
    this.options = (await fetch('api/categories')).json()
  }
}
</script>

<style scoped>

</style>
