<template>
  <div class="home">
    <h1>Home</h1>
    <div id='container' style="display:flex; flex-flow: row wrap; width: 70%;  margin:0 auto">
      <movie-card
        v-for="movie in movies"
        :key="movie.id"
        :movie = 'movie'
      ></movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import {mapState} from 'vuex'
export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

  },
  created: function() {
    this.$store.dispatch('LoadMovieCards', this.setToken())
  },
  computed: {
    ...mapState(['movies'])
  }
}
</script>