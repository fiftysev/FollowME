<template>
  <div class="grid min-h-screen place-items-center w-full">
    <div class="w-11/12 p-12 bg-green-400 rounded sm:w-8/12 md:w-1/2 lg:w-5/12">
      <h1 class="text-xl font-semibold"> Пожалуйста, заполните все поля: </h1>
      <form class="mt-6">
        <div class="flex justify-between gap-3">
        <span class="w-1/2">
          <label for="firstname" class="block text-xs font-semibold text-gray-600 uppercase">Имя</label>
          <input id="firstname" type="text" name="firstname" placeholder="Ivan" autocomplete="given-name" class="block w-full p-3 mt-2 text-gray-700 bg-gray-200 appearance-none focus:outline-none focus:bg-gray-300 focus:shadow-inner" required />
        </span>
          <span class="w-1/2">
          <label for="lastname" class="block text-xs font-semibold text-gray-600 uppercase">Фамилия</label>
        <input id="lastname" type="text" name="lastname" placeholder="Ivanov" autocomplete="family-name" class="block w-full p-3 mt-2 text-gray-700 bg-gray-200 appearance-none focus:outline-none focus:bg-gray-300 focus:shadow-inner" required />
        </span>
        </div>
        <label for="username" class="block mt-2 text-xs font-semibold text-gray-600 uppercase">Логин</label>
        <input id="username" type="text" name="username" placeholder="god_damn424" autocomplete="username" class="block w-full p-3 mt-2 text-gray-700 bg-gray-200 appearance-none focus:outline-none focus:bg-gray-300 focus:shadow-inner" required />
        <label for="password" class="block mt-2 text-xs font-semibold text-gray-600 uppercase">Пароль</label>
        <input id="password" type="password" name="password" placeholder="********" autocomplete="new-password" class="block w-full p-3 mt-2 text-gray-700 bg-gray-200 appearance-none focus:outline-none focus:bg-gray-300 focus:shadow-inner" required />
        <label for="password-confirm" class="block mt-2 text-xs font-semibold text-gray-600 uppercase">Подтверждение пароля</label>
        <input id="password-confirm" type="password" name="password-confirm" placeholder="********" autocomplete="new-password" class="block w-full p-3 mt-2 text-gray-700 bg-gray-200 appearance-none focus:outline-none focus:bg-gray-300 focus:shadow-inner" required />
        <button type="submit" class="w-full mt-5 py-2 tracking-widest uppercase">Зарегистрироваться</button>
        <p class="flex justify-between inline-block mt-4 text-xl italic text-gray-500 cursor-pointer hover:text-black">Уже есть аккаунт?</p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegistrationForm'
}
</script>

<style scoped>
  input {
    @apply rounded
  }
</style>
