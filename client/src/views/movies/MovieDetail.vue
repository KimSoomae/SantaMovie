<template>
  <div>
    <h1>MovieDetail</h1>
    <div class="card" style="width: 18rem; margin:0 auto" >
    <img :src="imgUrl" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title"><b>{{movie.title}}</b></h5>
      <p class="card-text">{{movie.overview}}</p>
      <!-- 예고편 -->
      <iframe :src="videoUrl" frameborder="0"></iframe>
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
import axios from 'axios'
export default {
  components: { CreateReview, ReviewList },
  name: 'MovieDetail', 
  data: function() {
    return {
      video_key: null,
      videoUrl: null,
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
    getpreview: function() {
      console.log(this.movie.id)
      axios({
        method: "GET",
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.movieId}/videos?api_key=f9acc36e1794da31c1fa05368571a14c&language=en-US`,
        headers: this.setToken()

      })
      .then(res => {
        if (res.data.results) {
          this.video_key = res.data.results[0].key
          this.videoUrl = `https://www.youtube.com/embed/${this.video_key}`
        }

      })
    },
    

  },
  
  created: function() {
    const config = this.setToken()
    const content = {
      token: config,
      movieId: this.$route.params.movieId
    }
    
    this.$store.dispatch('LoadMovieDetail', content)
    this.getpreview()
  },
  
  computed: {
    ...mapState(['movie']),
    imgUrl: function(){
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
},
  },

}
</script>

<style>

</style>