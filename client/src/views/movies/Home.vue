<template>
  <div class="home">
    <v-carousel
    cycle
    height="400"
    hide-delimiter-background
    show-arrows-on-hover
    >
    <v-carousel-item
      v-for="(slide, i) in slides"
      :key="i"
    >
      <v-sheet
        :color="colors[i]"
        height="100%"
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="text-h4" style="color: white; margin-top:20px;">
            Box Office 추천 영화
            <div id='container' style="display:flex; flex-flow: row wrap; width: 70%;  margin:0 auto; margin-left:-20px">
              <movie-card
                v-for="movie in movies.slice(i*5, i*5 + 5)"
                :key="movie.id"
                :movie = 'movie'
                
              ></movie-card>
           </div>
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
<h1>영화 추천</h1>
      <recommend-movie-card
        v-for="recommendmovie in recommendmovies"
        :key="recommendmovie.id"
        :recommendmovie = 'recommendmovie'
      ></recommend-movie-card>
<h1>크리스마스 영화</h1>
<christmas-movie-card
  v-for="christmasmovie in christmasmovies"
                :key="christmasmovie.id"
                :christmasmovie = 'christmasmovie'>
</christmas-movie-card>
</div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import {mapState} from 'vuex'
import axios from 'axios'
import RecommendMovieCard from '../../components/RecommendMovieCard.vue'
import ChristmasMovieCard from '../../components/ChristmasMovieCard.vue'
export default {
  name: 'Home',
  data () {
      return {
        recommendmovies: Array,
        colors: [
          'red darken-4',
          'green darken-4',
          'red darken-4',
          'green darken-4',
          'red darken-4',
          'green darken-4',
          'red darken-4',
        ],
        slides: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
          'Sixth',
          'Seventh'
        ],
      }
    },
  components: {
    MovieCard,
    RecommendMovieCard,
    ChristmasMovieCard,
  },
 
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    loadRecommendMovie: function() {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/accounts/get_recommend_movie/',
        headers: this.setToken()
        
      })
        .then(res => {
          this.recommendmovies = res.data
        })
        .catch(err => {
          console.log(err.response)
        })
    }

  },
  created: function() {
    this.$store.dispatch('LoadMovieCards', this.setToken())
    this.$store.dispatch('LoadChristmasMovieCards', this.setToken())
    this.loadRecommendMovie()
  },
  computed: {
    ...mapState(['movies']),
    ...mapState(['christmasmovies']),
  }
}
</script>