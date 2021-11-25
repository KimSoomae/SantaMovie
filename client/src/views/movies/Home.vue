<template>
  <div>
    
    
    <!-- <audio autoplay controls loop>
      <source src="@/audio/Mariah Carey-02-All I Want for Christmas Is You-Merry Christmas.mp3" type="audio/mpeg"> 브라우저가 audio 태그를 지원하지 않을 때 표시되는 문장
    </audio> -->
    <v-carousel v-model="model">
      <v-carousel-item
        v-for="(color, i) in colors"
        :key="color"
  
      >
        <v-sheet
          :color="color"
          height="100%"
          tile
  
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
            
          >
            <div class="text-h4" style="color: white; margin-top:0px;">
            Box Office 추천 영화
            
              <div class='container' style="display:flex; flex-flow: row wrap; width: 100%;  margin:0 auto; margin-left:-20px">
                <main class="page-content">
                <movie-card
                  v-for="movie in movies.slice(i*4, i*4 + 4)"
                  :key="movie.id"
                  :movie = 'movie'
                  
                ></movie-card>
                </main>
            </div>
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
       </v-carousel>
      <hr>
  <v-carousel v-model="model2">
      <v-carousel-item
        v-for="(color, i) in colors2"
        :key="i"
  
      >
        <v-sheet
          :color="color"
          height="100%"
          tile
  
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
            
          >
            <div class="text-h4" style="color: white; margin-top:20px;">
            취향저격 추천 영화
            
              <div class='container' style="display:flex; flex-flow: row wrap; width: 100%;  margin:0 auto; margin-left:-20px">
                <main class="page-content">
                <recommend-movie-card
            v-for="recommendmovie in recommendmovies.slice(i * 4, i * 4 + 4)"
            :key="recommendmovie.id"
            :recommendmovie = 'recommendmovie'
          ></recommend-movie-card>
                </main>
            </div>
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
<hr>
<v-carousel v-model="model">
      <v-carousel-item
        v-for="(color, i) in colors"
        :key="color"
  
      >
        <v-sheet
          :color="color"
          height="100%"
          tile
  
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
            
          >
            <div class="text-h4" style="color: white; margin-top:20px;">
            크리스마스 추천 영화
            
              <div class='container' style="display:flex; flex-flow: row wrap; width: 100%;  margin:0 auto; margin-left:-20px">
                <main class="page-content">
               
                <christmas-movie-card
                v-for="christmasmovie in christmasmovies.slice(i*4, i*4+4)"
                :key="christmasmovie.id"
                :christmasmovie = 'christmasmovie'>
                </christmas-movie-card>
                </main>
            </div>
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
       </v-carousel>
</div>
</template>

<script >
import MovieCard from '@/components/MovieCard'
import RecommendMovieCard from '@/components/RecommendMovieCard.vue'
import ChristmasMovieCard from '../../components/ChristmasMovieCard.vue'
import {mapState} from 'vuex'
import axios from 'axios'
export default {
  name: 'Test2',
  data () {
      return {
        model: 0,
        model2: 0,
        recommendmovies: Array,
        colors: [
          'rgb(131, 18, 22)',
          // 'red darken-4',
          'rgb(51, 77, 16)',
          'rgb(131, 18, 22)',
          'rgb(51, 77, 16)',
          'rgb(131, 18, 22)',
          'rgb(51, 77, 16)',
          'rgb(131, 18, 22)',
        ],
        colors2: [
          
          'rgb(51, 77, 16)',
          'rgb(131, 18, 22)',
          'rgb(51, 77, 16)',
          'rgb(131, 18, 22)',
          'rgb(51, 77, 16)',
          'rgb(131, 18, 22)',
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

<style scoped>

@import url('https://fonts.googleapis.com/css?family=Cardo:400i|Rubik:400,700&display=swap');
:root {
  --d: 700ms;
  --e: cubic-bezier(0.19, 1, 0.22, 1);
  --font-sans: 'Rubik', sans-serif;
  --font-serif: 'Cardo', serif;
}
* {
  box-sizing: border-box;
}
html, body { 
  height: 100%;
	/* width: 10px; */
}
body {
  display: grid;
  place-items: center;

}
.page-content {
  display: grid;
  grid-gap: 1rem;
  padding-left: 130px;
  padding-bottom: 50px;
  /* padding: 1rem; */
  max-width: 2024px;
  margin: 100 auto;
  font-family: var(--font-sans);
}
@media (min-width: 600px) {
  .page-content {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 800px) {
  .page-content {
		width: 100%;
    grid-template-columns: repeat(4, 1fr);
  }
}

.card {
	/*div에 이미지 꽉차게*/ 
	background-size: cover;
  position: relative;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
  padding: 1rem;
  width: 100%;
  text-align: center;
  color: whitesmoke;
  background-color: whitesmoke;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1), 0 2px 2px rgba(0, 0, 0, 0.1), 0 4px 4px rgba(0, 0, 0, 0.1), 0 8px 8px rgba(0, 0, 0, 0.1), 0 16px 16px rgba(0, 0, 0, 0.1);
}
@media (min-width: 600px) {
  .card {
    height: 350px;
  }
}
.card:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 110%;
  background-size: cover;
  background-position: 0 0;
  transition: transform calc(var(--d) * 1.5) var(--e);
  pointer-events: none;
}
.card:after {
  content: '';
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 200%;
  pointer-events: none;
  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.009) 11.7%, rgba(0, 0, 0, 0.034) 22.1%, rgba(0, 0, 0, 0.072) 31.2%, rgba(0, 0, 0, 0.123) 39.4%, rgba(0, 0, 0, 0.182) 46.6%, rgba(0, 0, 0, 0.249) 53.1%, rgba(0, 0, 0, 0.320) 58.9%, rgba(0, 0, 0, 0.394) 64.3%, rgba(0, 0, 0, 0.468) 69.3%, rgba(0, 0, 0, 0.540) 74.1%, rgba(0, 0, 0, 0.607) 78.8%, rgba(0, 0, 0, 0.668) 83.6%, rgba(0, 0, 0, 0.721) 88.7%, rgba(0, 0, 0, 0.762) 94.1%, rgba(0, 0, 0, 0.790) 100%);
  transform: translateY(-50%);
  transition: transform calc(var(--d) * 2) var(--e);
}
/* .card:nth-child(1):before{
	background-image: url("imgUrl")
} */
/* .card:nth-child(1):before {
  background-image: url(https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ);
}
.card:nth-child(2):before {
  background-image: url(https://images.unsplash.com/photo-1533903345306-15d1c30952de?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ);
}
.card:nth-child(3):before {
  background-image: url(https://images.unsplash.com/photo-1545243424-0ce743321e11?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ);
}
.card:nth-child(4):before {
  background-image: url(https://images.unsplash.com/photo-1531306728370-e2ebd9d7bb99?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ);
} */
.content {
  position: relative;
  display: inline-block;;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 1rem;
  transition: transform var(--d) var(--e);
  z-index: 1;
}
.content > p.overview{
	font-size: 1rem;
	overflow: hidden;
	text-overflow: ellipsis;
	/* white-space: nowrap; */
	width: 200px;
	display: -webkit-box;
	-webkit-line-clamp: 4; /* ellipsis line */
	-webkit-box-orient: vertical;
	/* height: 30px; */
	line-height: 1.2em;
}
.content > p.title{
	font-size:2rem;
	height:15px;
}
.content > p.des{
	font-size: 1rem;
	height: 10px;
}
.content > span.genre{
	text-align: center;
	width: 50px;
	font-size: 1rem;
	height: 10px;
	word-break : nowrap !important;
	z-index:-1;
}
.content > * + * {
  margin-top: 1rem;
}
.title {
  font-size: 0.6rem;
  font-weight: bold;
  line-height: 1.2;
}
.copy {
  font-family: var(--font-serif);
  font-size: 1.125rem;
  font-style: italic;
  line-height: 1.35;
}
.btn {
  cursor: pointer;
  margin-top: 1.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 0.65rem;
  font-weight: bold;
  letter-spacing: 0.025rem;
  text-transform: uppercase;
  color: white;
  background-color: black;
  border: none;
}
.btn:hover {
  background-color: #0d0d0d;
}
.btn:focus {
  outline: 1px dashed yellow;
  outline-offset: 3px;
}
@media (hover: hover) and (min-width: 600px) {
.card:after {
  transform: translateY(0);
}
.content {
  transform: translateY(calc(100% - 4.5rem));
}
.content > *:not(.title) {
  opacity: 0;
  transform: translateY(1rem);
  transition: transform var(--d) var(--e), opacity var(--d) var(--e);
}
.card:hover, .card:focus-within {
  align-items: center;
}
.card:hover:before, .card:focus-within:before {
  transform: translateY(-4%);
}
.card:hover:after, .card:focus-within:after {
  transform: translateY(-50%);
}
.card:hover .content, .card:focus-within .content {
  transform: translateY(0);
}
.card:hover .content > *:not(.title), .card:focus-within .content > *:not(.title) {
  opacity: 1;
  transform: translateY(0);
  transition-delay: calc(var(--d) / 8);
}
.card:focus-within:before, .card:focus-within:after, .card:focus-within .content, .card:focus-within .content > *:not(.title) {
  transition-duration: 0s;
  }
}
</style>