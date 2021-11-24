<template>
  <div>
    <!-- <input 
      type="text" 
      v-model="title" 
    >
    <input type="number" max="5" v-model="rank"> -->
    <span>
      <input class="clean-slide" id="age" type="text" v-model="title" placeholder="한줄평을 남겨주세요." /><label for="age">한줄평</label>
    </span> 
    <span> 
      <input class="clean-slide" id="num" type="number" v-model="rank" max="5" placeholder="평점을 매겨주세요." /><label for="rate">평점</label>
    </span>
    <v-btn
      class="ma-2"
      outlined
      large
      fab
      color="#7ab893"
      @click="createReview"
    >
      <v-icon>mdi-pencil</v-icon>
    </v-btn>
    <!-- <button @click="createReview" style="color:white;">+</button> -->

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateReview',
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
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    createReview: function () {
      const config = this.setToken()
      const content = {
      token: config,
      movieId: this.movie,
    }
      const reviewItem = {
        title: this.title,
        rank : this.rank
      }

      if (reviewItem.title) {
        console.log('여기까지 왔음')
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/movies/${this.movie}/reviews/`,
          data: reviewItem,
          headers: config,
        })
          .then(res => {
            console.log(res)
            this.$store.dispatch('LoadMovieDetail', content)
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
span {
    position: relative;
    display: inline-block;
    margin: 30px 10px;
  }
.clean-slide {
    position: relative;
    display: inline-block;
    width: 215px;
    padding: 10px 0 10px 15px;
    font-family: "Open Sans", sans;
    font-weight: 400;
    color: #377d6a;
    background: #efefef;
    border: 0;
    border-radius: 3px;
    outline: 0;
    text-indent: 60px;
    transition: all 0.3s ease-in-out;
}
.clean-slide::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
}
.clean-slide + label {
    display: inline-block;
    position: absolute;
    transform: translateX(0);
    top: 0;
    left: 0;
    bottom: 0;
    padding: 13px 15px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #032429;
    text-align: left;
    text-shadow: 0 1px 0 rgba(255, 255, 255, .4);
    transition: all 0.3s ease-in-out, color 0.3s ease-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    overflow: hidden;
}
.clean-slide + label:after {
    content: "";
    position: absolute;
    top: 0;
    right: 100%;
    bottom: 0;
    width: 100%;
    background: #7ab893;
    z-index: -1;
    transform: translate(0);
    transition: all 0.3s ease-in-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
}
.clean-slide:active,
.clean-slide:focus {
    color: #377d6a;
    text-indent: 0;
    background: #fff;
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}
.clean-slide:active::-webkit-input-placeholder,
.clean-slide:focus::-webkit-input-placeholder {
    color: #aaa;
}
.clean-slide:active + label,
.clean-slide:focus + label {
    color: #fff;
    text-shadow: 0 1px 0 rgba(19, 74, 70, .4);
    transform: translateX(-100%);
}
.clean-slide:active + label:after,
.clean-slide:focus + label:after {
    transform: translate(100%);
}

</style>





