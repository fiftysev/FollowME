import Vue from 'vue'
import App from './App.vue'
import Axios from 'axios'
import router from './router'
import './assets/styles/tailwind.css'
import vuetify from './plugins/vuetify'

Vue.prototype.$http = Axios
Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
