import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    rating: null,
    info: null,
  },
  getters: {
    rating: state => state.rating,
    info: state => state.info,
  },
  mutations: {
    setRating(state, rating) {
      state.rating = rating; // eslint-disable-line no-param-reassign
    },
    setInfo(state, info) {
      state.info = info; // eslint-disable-line no-param-reassign
    },
  },
  actions: {
    setRating({ commit }, rating) {
      commit(`setRating`, rating);
    },
    resetRating({ commit }) {
      commit(`setRating`, null);
    },
    setInfo({ commit }, info) {
      commit(`setInfo`, info);
    },
  },
});
