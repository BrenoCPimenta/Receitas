import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    rating: null
  },
  getters: {
    rating: state => state.rating
  },
  mutations: {
    setRating (state, rating) {
      state.rating = rating
    }
  },
  actions: {
    setRating ({ commit }, rating) {
      commit('setRating', rating)
    },
    resetRating ({ commit }) {
      commit('setRating', null)
    }
  },
});
