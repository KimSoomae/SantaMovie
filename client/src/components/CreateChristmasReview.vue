<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
    >
    <input type="number" max="5" v-model="rank">
  
    <button @click="createChristmasReview">+</button>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateChristmasReview',
  data: function () {
    return {
      title: null,
      rank: Number,
    }
  },
  props: {
    christmasmovie : {
      type: Number,
    }, 
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    createChristmasReview: function () {
      const config = this.setToken()
      const content = {
      token: config,
      christmasmovieId: this.christmasmovie,
    }
      const christmasreviewItem = {
        title: this.title,
        rank : this.rank
      }

      if (christmasreviewItem.title) {
        console.log('룰랄라')
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/christmasmovies/${this.christmasmovie}/christmasreviews/`,
          data: christmasreviewItem,
          headers: config,
        })
          .then(() => {
            this.$store.dispatch('LoadChristmasMovieDetail', content)
          })
          .catch(err => {
            console.log(err.response)
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





