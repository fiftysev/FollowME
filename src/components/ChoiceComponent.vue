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
    <v-btn
      v-if="selected"
      class="w-1/2 mt-4 px-3 font-bold"
      style="color: white; background: #5381b8"
    >
      <router-link
        tag="a"
        :to="{name: 'Place', params: {category: selected}}"
      >
        Начать поиск
      </router-link>
    </v-btn>

    <v-btn
      v-else
      @click="snackbar = true"
      class="w-1/2 mt-4 px-3 font-bold"
      style="color: white; background: #5381b8"
    >
      Начать поиск
    </v-btn>

    <v-snackbar
      v-model="snackbar"
      :multi-line="multiLine"

    >
      {{notSelectedExceptionMessage}}
      <template>
        <v-btn
          plain
          text
          :disabled="button_disabled"
          style="color: red"
          @click="snackbar = false"
        >
          Закрыть
        </v-btn>
      </template>
    </v-snackbar>
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
      ],
      notSelectedExceptionMessage: 'Чтобы осуществить поиск, выберите категорию.',
      multiLine: true,
      snackbar: false,
      button_disabled: false
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
