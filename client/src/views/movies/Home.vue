<template>
  <div class="home">
    <h1>Home</h1>
    <div id='container' style="display:flex; flex-flow: row wrap; width: 70%;  margin:0 auto">
      <movie-card
        v-for="movie in movies"
        :key="movie.id"
        :movie = 'movie'
      ></movie-card>

      <h1>영화 추천</h1>
      <recommend-movie-card
        v-for="recommendmovie in recommendmovies"
        :key="recommendmovie.id"
        :recommendmovie = 'recommendmovie'
      ></recommend-movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import {mapState} from 'vuex'
import axios from 'axios'
import RecommendMovieCard from '../../components/RecommendMovieCard.vue'
export default {
  name: 'Home',
  components: {
    MovieCard,
    RecommendMovieCard,
  },
  data: function() {
    return {
      recommendmovies: Array
    }
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    loadRecommendMovie: function() {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/accounts/get_recommend_movie/',
        headers: this.setToken()
        
      })
        .then(res => {
          this.recommendmovies = res.data
        })
        .catch(err => {
          console.log(err.response)
        })
    }

  },
  created: function() {
    this.$store.dispatch('LoadMovieCards', this.setToken())
    this.loadRecommendMovie()
  },
  computed: {
    ...mapState(['movies'])
  }
}
</script>