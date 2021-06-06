import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CardView from '@/views/CardView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/place/:category',
    name: 'Place',
    component: CardView,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
