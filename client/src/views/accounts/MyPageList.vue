<template>
  <div>
    <h3>내이름은{{username}}</h3>
    내가 좋아하는 영화는 {{moviePicks.title}}
  </div>
</template>


<script>
import axios from 'axios'


export default {
  name: 'MyPageList',
  data: function(){
    return{
      username: null,
      moviePicks: 
        {
          title: null,
          poster_path: null,
        },
      
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
    saveMoviePick: function(movie_id) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/save-movie/${movie_id}/`,
        headers: this.setToken(), // Authorization: JWT token값
      })
      .then(res => {
        console.log(res)
        this.$router.push({name:'Home'})
      })

    },
   
  },
  created: function () {
    axios({
      method : 'get',
      url: 'http://127.0.0.1:8000/accounts/get-user/',
      headers: this.setToken()
    })
    .then(res => {
      // list로 들어옴
      console.log(res.data)
      this.username = res.data.username
      this.moviePicks.title = res.data.moviepicks.title
      this.moviePicks.poster_path = res.data.moviepicks.poster_path
      //this.moviePicks = res.data

    })
    .catch(err => {
          console.log(err)
        })
  }
}
</script>

<style>

</style>