<template>
  <div class="card" style="width: 18rem; margin:0 auto" >
<div @click="moveToMovieDetail">
    <img :src="imgUrl" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title"><b>{{recommendmovie.title}}</b></h5>
      <p class="card-text">{{recommendmovie.overview}}</p>
      <p>{{recommendmovie.popularity}}</p>
      <p v-for="genre in recommendmovie.genre_ids" :key="genre.id">{{genre.name}}</p>
      </div>
      </div>
      <button @click="likeMovie"> 좋아요 </button>
      {{key}} -- {{like_users}}
  </div>

</template>

<script>
import axios from 'axios'
export default {
  name: 'RecommendationMovieCard',
  props: {
    recommendmovie : {
      type: Object,
    }, 
  },
  data: function() {
    return {
      key: Boolean,
      like_users: Number,
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

    moveToMovieDetail: function() {
      this.$router.push({ name: 'MovieDetail', params: {movieId: this.recommendmovie.id}})

    },
    likeMovie: function() {
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/movies/${this.recommendmovie.id}/like/`,
        headers: this.setToken(),
      })
        .then((res) => {
            this.key = res.data.key
            this.like_users = res.data.like_users
          })
          .catch(err => {
            console.log(err)
          })
    },
    getLikes: function() {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/movies/${this.recommendmovie.id}/like/`,
        headers: this.setToken(),
      })
        .then((res) => {
          // console.log(res)
          this.key = res.data.key
          this.like_users = res.data.like_users
          })
          .catch(err => {
            console.log(err)
          })
    }

  },
  created: function() {
    this.getLikes()
  },

  computed: {
    imgUrl: function(){
      return `https://image.tmdb.org/t/p/w500/${this.recommendmovie.poster_path}`

}
  }
}
</script>

<style>

</style>