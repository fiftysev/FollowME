<template>
  <div class="card w-64 md:w-96 xl:h-48 xl:w-128 bg-green-400 py-5 rounded-md flex flex-col items-center">
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
      class="w-2/3 mt-4 xl:mt-10 px-3 font-bold"
      style="color: white; background: #5381b8"
      @click="handleSearch"
    >
        Начать поиск
    </v-btn>

    <v-snackbar
      v-model="snackbar"
      :multi-line="multiLine"
      min-width="260"

    >
      {{notSelectedExceptionMessage}}
      <template>
        <v-btn
          plain
          text
          :disabled="button_disabled"
          style="color: #60c5fc"
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
  methods: {
    handleSearch () {
      if (!this.selected) {
        this.snackbar = true
        return
      }
      this.$router.push(`/place/${this.selected}`)
      this.selected = null
      this.snackbar = false
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
