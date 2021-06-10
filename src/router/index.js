/* eslint-disable */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CardView from '@/views/CardView'
import RegistrationForm from '@/components/RegistrationForm'
import AuthUserBoard from '@/components/AuthUserBoard'
import LoginForm from '@/components/LoginForm'
import store from '../store/index'

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
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LoginForm,
    meta: {
      guest: true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuth) {
      next()
      return
    }
    next('/')
  } else {
    next()
  }
})

export default router
