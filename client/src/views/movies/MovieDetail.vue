<template>
  <div>
    <h1>MovieDetail</h1>
    <div class="card" style="width: 18rem; margin:0 auto" >
    <img :src="imgUrl" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title"><b>{{movie.title}}</b></h5>
      <p class="card-text">{{movie.overview}}</p>
      <!-- 주연배우, 예고편 -->
      <p v-for="genre in movie.genre_ids" :key="genre.id">{{genre.name}}</p>
      <p v-for="actor in movie.movie_actor" :key='actor.id'>{{actor.name}}</p>
      <p>{{movie.release_date}}</p>
      <p>{{movie.popularity}}</p>
    </div>
     <review-list :reviews="movie.movie_review" :movieid ="movie.id"></review-list>
  </div>
  <create-review :movie ="movie.id"></create-review>

  
  </div>
</template>

<script>
import {mapState} from 'vuex'
import CreateReview from '@/components/CreateReview.vue'
import ReviewList from '@/components/ReviewList.vue'
export default {
  components: { CreateReview, ReviewList },
  name: 'MovieDetail', 
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
    const config = this.setToken()
    const content = {
      token: config,
      movieId: this.$route.params.movieId
    }
    
    this.$store.dispatch('LoadMovieDetail', content)
  },
  
  computed: {
    ...mapState(['movie']),
    imgUrl: function(){
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`

}
  },

}
</script>

<style>

</style>