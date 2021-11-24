<template>
  <div>
    {{christmasreview.title}} -- {{christmasreview.rank}}
    <button>수정</button>
    <button @click="deleteChristmasReview">삭제</button>
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