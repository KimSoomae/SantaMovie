<template>
  <div>
    {{review.title}} -- {{review.rank}}
    <button>수정</button>
    <button @click="deleteReview">삭제</button>
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
    deleteReview: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/movies/reviews/${this.review.id}/`,
      })
        .then(res => {
          console.log('예쓰')
            console.log(res)
            this.$store.dispatch('LoadMovieDetail', this.movieid)
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