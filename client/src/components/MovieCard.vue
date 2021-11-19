<template>
  <div class="card" style="width: 18rem; margin:0 auto" @click="moveToMovieDetail">
    <img :src="imgUrl" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title"><b>{{movie.title}}</b></h5>
      <p class="card-text">{{movie.overview}}</p>
      <p>{{movie.popularity}}</p>
      <p v-for="genre in movie.genre_ids" :key="genre.id">{{genre.name}}</p>
    </div>
  </div>

</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie : {
      type: Object,

    }, 
  },
  methods: {
    moveToMovieDetail: function() {
      this.$router.push({ name: 'MovieDetail', params: {movieId: this.movie.id}})

    }

  },
  computed: {
    imgUrl: function(){
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`

}
  }
}
</script>

<style>

</style>