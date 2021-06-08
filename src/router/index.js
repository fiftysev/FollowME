/* eslint-disable */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CardView from '@/views/CardView'
import RegistrationForm from '@/components/RegistrationForm'
import AuthUserBoard from '@/components/AuthUserBoard'

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
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: RegistrationForm,
    meta: {
      guest: true
    }
  },
  {
    path: '/userboard',
    name: 'UserBoard',
    component: AuthUserBoard,
    meta: {
      requiresAuth: true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('jwt') == null) {
      next({
        path: '/signup',
        params: { nextUrl: to.fullPath }
      })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (localStorage.getItem('jwt') == null) {
      next()
    } else {
      next({ name: 'UserBoard'})
    }
  } else {
    next()
  }
})

export default router
