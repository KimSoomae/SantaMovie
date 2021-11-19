import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    movie: [],
    // reviews: []
  },
  mutations: {
    LOAD_MOVIE_CARDS: function(state, movies){
      state.movies = movies
    },
    LOAD_MOVIE_DETAIL: function(state,movie){
      state.movie = movie
    },
    // CREATE_REVIEW: function(state,review){
    //   state.reviews.push(review)
    // }
  },
  actions: {
    LoadMovieCards: function({commit}) {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/movies',
      })
        .then((res) => {
          //console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data)
        })

    },
    LoadMovieDetail: function({commit},movieId) {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/movies/${movieId}`,
      })
        .then((res) => {
          //console.log(res)
          commit('LOAD_MOVIE_DETAIL',res.data)
        })

    },
    // createReview: function({commit}, context) {
    //   axios({
    //     method:'post',
    //     url: `http://127.0.0.1:8000/movies/movies/${context[1]}/reviews/`,
    //     data: context[0]
    //   })
    //    .then(res => {
    //      console.log(res)
    //      commit('CREATE_REVIEW', res.data)
    //    })
    //    .catch(err => {
    //      console.log(err)
    //    })
    // }
  },
  modules: {
  }
})

