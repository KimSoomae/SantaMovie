<template>
  <div>
			<div class="wrapper" style="width: 10rem; margin:0 auto; margin-right:60px;" >
				<ul class="stage clearfix">

					<li class="scene">
            <!-- onclick="return true" -->
            <div class="movie" onclick="return true" @click="moveToMovieDetail">
              <img class="poster" :src="imgUrl" alt="..." >
                <div class="info">
                    <header>
                        <h3>{{movie.title}}</h3>
                        <h5 class="year">{{movie.popularity}}</h5>
                        <h5 v-for="genre in movie.genre_ids" :key="genre.id">{{genre.name}}</h5>
                        <h6>{{movie.overview}}</h6>
                        <button @click="likeMovie"> 좋아요 </button>
                        {{key}} -- {{like_users}}
                    </header>
                    
                  
             </div>
            </div>
         
     
					</li>
          
				</ul>
			</div><!-- /wrapper -->
		


  <!-- <div class="card" style="width: 10rem; margin:0 auto" >
    <div @click="moveToMovieDetail">
        <img :src="imgUrl" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title"><b>{{movie.title}}</b></h5>
          <p class="card-text">{{movie.overview}}</p>
          <p>{{movie.popularity}}</p>
          <p v-for="genre in movie.genre_ids" :key="genre.id">{{genre.name}}</p>
          </div>
      </div>
      <button @click="likeMovie"> 좋아요 </button>
      {{key}} -- {{like_users}}
  </div> -->
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieCard',
  props: {
    movie : {
      type: Object,

    }, 
  },
  data: function() {
    return {
      key: Boolean,
      like_users: Number,

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

    moveToMovieDetail: function() {
      this.$router.push({ name: 'MovieDetail', params: {movieId: this.movie.id}})

    },
    likeMovie: function() {
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res)
          this.key = res.data.key
          this.like_users = res.data.like_users
          })
          .catch(err => {
            console.log(err)
          })
    },
    getLikes: function() {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: this.setToken(),
      })
        .then((res) => {
          //console.log(res)
          this.key = res.data.key
          this.like_users = res.data.like_users
          })
          .catch(err => {
            console.log(err)
          })
    }

  },
   created: function() {
    this.getLikes()
  },
  computed: {
    imgUrl: function(){
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`

}
  }
}
</script>

<style>
*, *:after, *:before { -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; }

body {
	background: darkblue;
	font-family: 'Lato', Arial, sans-serif;
	color: #fff;
}

.wrapper {
	margin: 0 auto 100px auto;
	max-width: 960px;
}

.stage {
	list-style: none;
	padding: 0;
}

/*************************************
Build the scene and rotate on hover
**************************************/

.scene {
	width: 260px;
	height: 400px;
	margin: 30px;
	float: left;
	-webkit-perspective: 1000px;
	-moz-perspective: 1000px;
	perspective: 1000px;
}

.movie {
	width: 260px;
	height: 400px;
	-webkit-transform-style: preserve-3d;
	-moz-transform-style: preserve-3d;
	transform-style: preserve-3d;
	-webkit-transform: translateZ(-130px);
	-moz-transform: translateZ(-130px);
	transform: translateZ(-130px);
	-webkit-transition: -webkit-transform 350ms;
	-moz-transition: -moz-transform 350ms;
	transition: transform 350ms;
}

.movie:hover {
	-webkit-transform: rotateY(-78deg) translateZ(20px);
	-moz-transform: rotateY(-78deg) translateZ(20px);
	transform: rotateY(-78deg) translateZ(20px);
}

/*************************************
Transform and style the two planes
**************************************/

.movie .poster, 
.movie .info {
	position: absolute;
	width: 200px;
	height: 300px;
	background-color: #fff;
	-webkit-backface-visibility: hidden;
	-moz-backface-visibility: hidden;
	backface-visibility: hidden;
}

.movie .poster  {
	-webkit-transform: translateZ(130px);
	-moz-transform: translateZ(130px);
	transform: translateZ(130px);
	background-size: cover;
	background-repeat: no-repeat;
}

.movie .info {
	-webkit-transform: rotateY(90deg) translateZ(130px);
	-moz-transform: rotateY(90deg) translateZ(130px);
	transform: rotateY(90deg) translateZ(130px);
	border: 1px solid #B8B5B5;
	font-size: 0.75em;
}

/*************************************
Shadow beneath the 3D object
**************************************/

.csstransforms3d .movie::after {
	content: '';
	width: 260px;
	height: 260px;
	position: absolute;
	bottom: 0;
	box-shadow: 0 30px 50px rgba(0,0,0,0.3);
	-webkit-transform-origin: 100% 100%;
	-moz-transform-origin: 100% 100%;
	transform-origin: 100% 100%;
	-webkit-transform: rotateX(90deg) translateY(130px);
	-moz-transform: rotateX(90deg) translateY(130px);
	transform: rotateX(90deg) translateY(130px);
	-webkit-transition: box-shadow 350ms;
	-moz-transition: box-shadow 350ms;
	transition: box-shadow 350ms;
}

.csstransforms3d .movie:hover::after {
	box-shadow: 20px -5px 50px rgba(0,0,0,0.3);
}

/*************************************
Movie information
**************************************/

.info header {
	color: #FFF;
	padding: 7px 10px;
	font-weight: bold;
	height: 195px;
	background-size: contain;
	background-repeat: no-repeat;
	text-shadow: 0px 1px 1px rgba(0,0,0,1);
}

.info header h1 {
	margin: 0 0 2px;
	font-size: 1.4em;
}

.info header .rating {
	border: 1px solid #FFF;
	padding: 0px 3px;
}

.info p {
	padding: 1.2em 1.4em;
	margin: 2px 0 0;
	font-weight: 700;
	color: #666;
	line-height: 1.4em;
	border-top: 10px solid #555;
}

/*************************************
Generate "lighting" using box shadows
**************************************/

.movie .poster,
.movie .info,
.movie .info header {
	-webkit-transition: box-shadow 350ms;
	-moz-transition: box-shadow 350ms;
	transition: box-shadow 350ms;
}

.csstransforms3d .movie .poster {
	box-shadow: inset 0px 0px 40px rgba(255,255,255,0);
}

.csstransforms3d .movie:hover .poster {
	box-shadow: inset 300px 0px 40px rgba(255,255,255,0.8);
}

.csstransforms3d .movie .info, 
.csstransforms3d .movie .info header {
	box-shadow: inset -300px 0px 40px rgba(0,0,0,0.5);
}

.csstransforms3d .movie:hover .info, 
.csstransforms3d .movie:hover .info header {
	box-shadow: inset 0px 0px 40px rgba(0,0,0,0);
}

/*************************************
Posters and still images
**************************************/

.scene:nth-child(1) .movie .poster {
  background-image: url(http://gallery.oneindia.in/ph-big/2013/09/aarambam-audio-launch-english-poster_137940737010.jpg);
}

.scene:nth-child(2) .poster {
  background-image: url(http://www.diehardvijayfans.com/wp-content/uploads/2013/08/thalaiva11413_m.jpg);
}

.scene:nth-child(3) .poster {
  background-image: url(http://static.rogerebert.com/uploads/movie/movie_poster/ram-leela-2013/large_7Xry4ghR6tPMS9DzFLblYRizV3.jpg);
}

.scene:nth-child(1) .info header {
	background-image: url(http://timesofcity.com/wp-content/uploads/2013/11/Aarambam-19-Days-Collections.jpg);
}

.scene:nth-child(2) .info header {
	background-image: url(http://media.chakpak.com/sites/default/files/styles/photoessay/public/Thalaiva-Movie-Posters.jpg);
}

.scene:nth-child(3) .info header {
	background-image: url(http://bollyspice.com/wp-content/uploads/2013/11/13nov_Ranveer-RamLeela05.jpg);
}

/*************************************
Fallback
**************************************/
.no-csstransforms3d .movie .poster, 
.no-csstransforms3d .movie .info {
	position: relative;
}

/*************************************
Media Queries
**************************************/
@media screen and (max-width: 60.75em){
	.scene {
		float: none;
		margin: 30px auto 60px;
	}
}

</style>