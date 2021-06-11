import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
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
            axios.defaults.headers.common['x-access-token'] = token
            commit('auth_success', token)
            commit('user_success', user)
            resolve(res)
          })
          .catch(err => {
            commit('auth_error')
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
            axios.defaults.headers.common['x-access-token'] = token
            commit('auth_success', token)
            commit('user_success', user)
            resolve(res)
          })
          .catch(err => {
            commit('auth_error', err)
            reject(err)
          })
      })
    },
    logout ({ commit }) {
      return new Promise((resolve, reject) => {
        commit('logout')
        delete axios.defaults.headers.common['x-access-token']
        resolve()
      })
    }
  },
  getters: {
    isAuth: state => !!state.token,
    authStatus: state => state.status,
    authedUser: state => state.user
  }
})
