<template>
  <div class="card w-1/4 bg-green-400 py-5 rounded-md flex flex-col items-center">
    <select
      name="placepicker"
      id="place"
      v-model="selected"
      class="w-11/12 bg-white bg-opacity-30"
    >
      <option
        v-bind:value="option.value"
        v-for="option in options"
        :key="option.id"
      >
        {{option.text}}
      </option>
    </select>
    <router-link
      tag="a"
      :to="{name: 'Place', params: {category: selected}}"
      class="button"
    >
      Начать поиск
    </router-link>
    <span
      class="font-bold text-white underline mt-3 cursor-pointer"
    >Отменить выбор</span>
  </div>
</template>

<script>
export default {
  name: 'ChoiceComponent',
  data () {
    return {
      selected: null,
      options: [
        { id: 1, value: 'bar', text: 'Бары' }
      ]
    }
  },
  async created () {
    const response = await fetch('/api/categories')
    this.options = await response.json()
  }
}
</script>

<style scoped>

</style>
