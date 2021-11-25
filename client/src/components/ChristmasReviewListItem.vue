<template>
  <div>
    {{christmasreview.title}} ({{christmasreview.rank}}점)
        <v-btn
              color="error"
              fab
              x-small
              dark
              @click="deleteChristmasReview"
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
  name: 'ChristmasReviewListItem',
  props: {
    christmasreview: Object,
    christmasmovieid: Number,
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteChristmasReview: function() {
      const config = this.setToken()
      const content = {
      token: config,
      christmasmovieId: this.christmasmovieid
    }
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/movies/christmasreviews/${this.christmasreview.id}/`,
        headers: this.setToken(),
      })
        .then(() => {
            this.$store.dispatch('LoadChristmasMovieDetail', content)
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