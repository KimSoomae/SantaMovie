<template>
  <div>
    {{review.title}} ({{review.rank}}점)
        <v-btn
              color="error"
              fab
              x-small
              dark
              @click="deleteReview"
              style="text-align:center;"
            >
              <v-icon>X</v-icon>
            </v-btn>
    <!-- </div> -->
    <!-- <button @click="deleteReview">삭제</button> -->
    <!-- modal -->
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
    movieid: Number,
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteReview: function() {
      const config = this.setToken()
      const content = {
      token: config,
      movieId: this.movieid
    }
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/movies/reviews/${this.review.id}/`,
        headers: this.setToken(),
      })
        .then(() => {
            this.$store.dispatch('LoadMovieDetail', content)
          })
          .catch(err => {
            console.log(err)
          })
    }
  }


}
</script>

<style>

</style>