<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
    >
    <input type="number" max="5" v-model="rank">
  
    <button @click="createReview">+</button>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
      rank: Number,
    }
  },
  props: {
    movie : {
      type: Number,
    }, 
  },
  methods: {
    createReview: function () {
      const reviewItem = {
        title: this.title,
        rank : this.rank
      }

      if (reviewItem.title) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/movies/${this.movie}/reviews/`,
          data: reviewItem,
        })
          .then(res => {
            console.log(res)
            this.$store.dispatch('LoadMovieDetail', this.movie)
            // this.$router.push({ name: 'TodoList' })
          })
          .catch(err => {
            console.log(err)
          })
        this.title = null
        this.rank = 0
      }
    }
}
}
</script>

<style scoped>

</style>





