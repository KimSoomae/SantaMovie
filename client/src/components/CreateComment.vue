<template>
  <div>
 <div class="row1">
  <span>
    <input @keyup.enter="createComment" class="balloon" id="state" type="text" placeholder="댓글을 작성 후 Enter를 눌러주세요." v-model="title"  /><label for="state" >Comment</label>
  </span>
  <!-- <b-button @click="createComment">+</b-button> -->
</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateComment',
  data: function () {
    return {
      title: null,
    }
  },
  props: {
    community : {
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

    createComment: function () {
      // const config = this.setToken()
    //   const content = {
    //   token: config,
    //   communityId: this.community,
    // }
      const commentItem = {
        title: this.title,
      }

      if (commentItem.title) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/community/${this.community}/comments/`,
          data: commentItem,
          headers: this.setToken(),
        })
          .then((res) => {
            console.log(res)
            this.$router.go(this.$router.currentRoute)
            
          })
          .catch(err => {
            console.log(err)
          })
        this.title = null
      }
    }
}
}
</script>

<style scoped>
* {
    box-sizing: border-box;
}
body,
html {
    overflow-x: hidden;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 300;
    color: #fff;
    background: #efefef;
}
.row1 {
    max-width: 800px;
    margin: 0 auto;
    padding: 30px 15px;
    /* background: #032429; */
    position: relative;
    z-index: 1;
    text-align: center;
    left: -100px;

}
.row1:before {
position: absolute;
content: "";
display: block;
top: 0;
left: -3000px;
height: 100%;
width: 15000px;
z-index: -1;
background: inherit;
}
.row1:first-child {
padding-top: 20px; 
padding-bottom: 0px;
}
.row1:nth-child(10),
.row1:nth-child(2),
.row1:nth-child(8) {
/* background: #134a46; */
}
.row1:nth-child(3),
.row1:nth-child(7) {
/* background: #377d6a; */
}
.row1:nth-child(4),
.row1:nth-child(6) {
background: #7ab893;
}
.row1:nth-child(5) {
background: #b2e3af;
}
.row1 span {
width: 50%;
position: relative;
display: inline-block;
margin: 30px 10px;
}

.state {
  color: red;
}

.balloon {

    display: inline-block;
    width: 600px;
    padding: 10px 0 10px 15px;
    font-family: "Open Sans", sans;
    font-weight: 400;
    /* color: #377d6a; */
    background: #efefef;
    border: 0;
    border-radius: 3px;
    outline: 0;
    text-indent: 60px;
    transition: all 0.3s ease-in-out;
}
.balloon::-webkit-input-placeholder {

    color: #efefef;
    text-indent: 0;
    font-weight: 300;
}
.balloon + label {
    display: inline-block;
    position: absolute;
    top: 8px;
    left: 0;
    bottom: 8px;
    padding: 5px 15px;
    color: #032429;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    text-shadow: 0 1px 0 rgba(19, 74, 70, 0);
    transition: all 0.3s ease-in-out;
    border-radius: 3px;
    background: rgba(122, 184, 147, 0);
}
.balloon + label:after {
    position: absolute;
    content: "";
    width: 0;
    height: 0;
    top: 100%;
    left: 50%;
    margin-left: -3px;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-top: 3px solid rgba(122, 184, 147, 0);
    transition: all 0.3s ease-in-out;
}
.balloon:active,
.balloon:focus {
    color: #377d6a;
    text-indent: 0;
    background: #fff;
}
.balloon:active::-webkit-input-placeholder,
.balloon:focus::-webkit-input-placeholder {
    color: rgb(6, 65, 35);
}
.balloon:active + label,
.balloon:focus + label {
    color: #fff;
    text-shadow: 0 1px 0 rgba(19, 74, 70, .4);
    background: rgba(122, 184, 147, 1);
    transform: translateY(-40px);
}
.balloon:active + label:after,
.balloon:focus + label:after {
    border-top: 4px solid rgba(122, 184, 147, 1);
}

</style>





