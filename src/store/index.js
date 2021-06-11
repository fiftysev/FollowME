import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: '',
    user: {}
  },
  mutations: {
    auth_request (state) {
      state.status = 'loading'
    },
    auth_success (state, token) {
      state.status = 'success'
      state.token = token
    },
    user_success (state, user) {
      state.user = user
    },
    auth_error (state) {
      state.status = 'error'
    },
    logout (state) {
      state.status = ''
      state.token = ''
    }
  },
  actions: {
    login ({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'auth/login', data: user, method: 'POST' })
          .then(res => {
            const token = res.data.token
            const user = res.data.user
            localStorage.setItem('token', token)
            axios.defaults.headers.common['x-access-token'] = token
            commit('auth_success', token)
            commit('user_success', user)
            resolve(res)
          })
          .catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    register ({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'auth/register', data: user, method: 'POST' })
          .then(res => {
            const token = res.data.token
            const user = res.data.user
            localStorage.setItem('token', token)
            axios.defaults.headers.common['x-access-token'] = token
            commit('auth_success', token)
            commit('user_success', user)
            resolve(res)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    logout ({ commit }) {
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['x-access-token']
        resolve()
      })
    }
  },
  getters: {
    isAuth: state => !!state.token,
    authStatus: state => state.status,
    authedUser: state => state.user.json()
  }
})
