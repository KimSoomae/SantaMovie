import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    movie: [],
    username: null,
  },
  mutations: {
    LOAD_MOVIE_CARDS: function(state, movies){
      state.movies = movies
    },
    LOAD_MOVIE_DETAIL: function(state,movie){
      state.movie = movie
    },
    GET_USER_NAME: function(state, user) {
      state.username = user
    }
    
  },
  actions: {
    LoadMovieCards: function({commit},token) {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/movies',
        headers: token
      })
        .then((res) => {
          //console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data)
        })

    },
    LoadMovieDetail: function({commit},content) {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/movies/${content.movieId}`,
        headers: content.token
      })
        .then((res) => {
          //console.log(res)
          commit('LOAD_MOVIE_DETAIL',res.data)
        })

    },
    GetUserName: function({commit},content) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/getuser/${content.userid}`,
        headers: content.token
      })
        .then((res) => {
          console.log(res)
          commit('GET_USER_NAME', res.data.username)
        } )
    }
 
  },
  modules: {
  }
})

