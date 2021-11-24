<template>
  <div>
    <h1>MovieDetail</h1>
    <div class="card" style="width: 18rem; margin:0 auto" >
    <img :src="imgUrl" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title"><b>{{christmasmovie.title}}</b></h5>
      <p class="card-text">{{christmasmovie.overview}}</p>
      <!-- 예고편 -->
      <iframe :src="videoUrl" frameborder="0"></iframe>
      <p v-for="genre in christmasmovie.genre_ids" :key="genre.id">{{genre.name}}</p>
      <p>{{christmasmovie.release_date}}</p>
      <p>{{christmasmovie.popularity}}</p>
    </div>
     <christmas-review-list :christmasreviews="christmasmovie.christmasmovie_review" :christmasmovieid ="christmasmovie.id"></christmas-review-list>
  </div>
  <create-christmas-review :christmasmovie ="christmasmovie.id"></create-christmas-review>

  
  </div>
</template>

<script>
import {mapState} from 'vuex'
import CreateChristmasReview from '@/components/CreateChristmasReview.vue'
import ChristmasReviewList from '@/components/ChristmasReviewList.vue'
import axios from 'axios'
export default {
  components: { CreateChristmasReview, ChristmasReviewList },
  name: 'ChristmasMovieDetail', 
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
      axios({
        method: "GET",
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.christmasmovieId}/videos?api_key=f9acc36e1794da31c1fa05368571a14c&language=en-US`,
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
      christmasmovieId: this.$route.params.christmasmovieId
    }
    
    this.$store.dispatch('LoadChristmasMovieDetail', content)
    this.getpreview()
  },
  
  computed: {
    ...mapState(['christmasmovie']),
    imgUrl: function(){
      return `https://image.tmdb.org/t/p/w500/${this.christmasmovie.poster_path}`
},
  },

}
</script>

<style>

</style>