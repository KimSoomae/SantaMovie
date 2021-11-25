<!--<template>
  <div>
    <h1>끌리는 영화를 선택해주세요</h1>
    <ul>
      <li v-for="movie in moviePicks" :key="movie.id">
        <img style="width: 200px" @click="saveMoviePick(movie.id)" :src="movie.poster_path" alt="..">
        <p>{{movie.title}}</p>
      </li>
    </ul>
    
  </div>
</template> -->
<template>
<div>
  <h1>끌리는 영화를 5개 선택해주세요!</h1>
  <!-- <h3>{{cnt}}</h3> -->
  <br>
  <v-card
    class="mx-auto"
    max-width="1300"
  >

    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="card in moviePicks"
          :key="card.id"
          :cols=3
        >
          <v-card>
            <v-img
              :src="card.poster_path"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="400px"
            >
              <v-card-title v-text="card.title"></v-card-title>
            </v-img>

            <v-card-actions>
              <v-spacer></v-spacer>
              <div @click="saveMoviePick(card.id)">
              <v-btn icon>
                <v-icon color="red" size="35px" >mdi-heart</v-icon>
              </v-btn>
              </div>

            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'MyPage',
  data: function(){
    return{
      cnt : 1,
      moviePicks: 
        {
          title: null,
          poster_path: null,
        },
      //user: this.$session.set('user_no', res.user_no)
      
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
      //onsole.log(movie)

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/save-movie/${movie_id}/`,
        headers: this.setToken(), // Authorization: JWT token값
      })
      .then(() => {
        this.cnt = this.cnt * 2
        if (this.cnt === 32) {
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/save_user_genre/',
            headers: this.setToken(),
          })
            .then(res=>{
              console.log(res)
            })
            .catch (err => {
              console.log(err)
            })
          this.$router.push({name:'Home'})
        }
        
      })

    },
    showCommunity: function(){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/community/`,
      })
    }
  },
  created: function () {
    axios({
      method : 'get',
      url: 'http://127.0.0.1:8000/accounts/get-pick-movie/',
    })
    .then(res => {
      // list로 들어옴
      console.log(res.data)
      this.moviePicks = res.data

    })
    .catch(err => {
          console.log(err)
        })
  }
}
</script>

<style scoped>
  h1 {
    color: #ccc7c7;
  }
</style>