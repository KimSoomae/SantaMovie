<template>
<div>
  <h1 class="h1font">{{community.id}}번 게시글</h1>
  <div class="blog py-5">
    <div class="container">
      <div class="row">
        <div class=" mx-auto px-0 bg-white shadow-sm rounded itiscard">
          <div class="col-lg-5  float-md-left blog-thumbnail" style="background-image: url('https://media.vlpt.us/images/easycheaploansuk/post/e7865b20-64df-4117-9b73-d824d60bfe97/christmas.jpg')"></div>
          <div class="col-lg-7  float-md-left">
            <div class="p-3 p-sm-5 boxbox">
              <div class="mb-4">
                <h1 class="mb-4">
                  {{community.title}}
                </h1>
                <div class="mb-0">
                <h4>{{community.content}}</h4>
                <hr>
                <br>
                글쓴 시간: {{community.updated_at}}
                <br>
              
                글쓴이: {{username}}
                </div>
                <br>
                <div>
                  <h4>
                <span class="text-success" v-for="tag in community.tags" :key="tag.id">#{{tag.name}}  </span>
     </h4>
<br></div>
<v-btn tile="tile" color="success" @click="updateCommunity" v-if="flag">
<v-icon left="left">
    mdi-pencil
</v-icon>
Edit
</v-btn>
<v-btn tile="tile" color="error" @click="deleteCommunity" v-if="flag">
<v-icon left="left">
    mdi-minus-circle
</v-icon>
DELETE
</v-btn>
</div>
</div>
</div>
</div>
</div>
</div>
  </div>
    <create-comment :community ="community.id"></create-comment>
   <comment-list :comments="community.comments"></comment-list>
  
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '../../components/CommentList.vue'
import CreateComment from '../../components/CreateComment.vue'
import {mapState} from 'vuex'
export default {
  components: { CommentList, CreateComment },
  name: 'CommunityDetail',
  data: function () {
    return {
      community: Object,
      flag: Boolean
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
    getCommunityDetail: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.$route.params.communityId}`,
        headers: this.setToken(), // Authorization: JWT token값
      })
        .then(res => {
          this.community = res.data
         console.log('나다',this.community)
          const content = {
            token: this.setToken(),
            userid: this.community.user
          }
          this.$store.dispatch('GetUserName', content)
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/check_same_user/${this.community.user}/`,
            headers: this.setToken()
          })
            .then(res => {
              this.flag = res.data.flag
              console.log(res)
        })
            .catch(err => {
            console.log(err)
          })
        })
            .catch(err => {
            console.log(err)
        })
        
    },
    deleteCommunity: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.community.id}/`,
        headers: this.setToken(),
      })
        .then(() => {
          // console.log(res)
          this.$router.push({name: 'Community'})
          })
          .catch(err => {
            console.log(err)
          })
    },
    updateCommunity: function() {
      this.$router.push({name: 'UpdateCommunity', params: {communityId: this.community.id}} )
    },
    checkSameUser: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/check_same_user/${this.community.user}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
        })
    }
  
  },
  computed: {
    ...mapState(['username'])
  },
  created: function () {
    if (localStorage.getItem('jwt')){
        this.getCommunityDetail()
        this.checkSameUser()
    }
    else{
      this.$router.push({name: 'Login'})
    }
    
  }
}
</script>

<style scoped>
@charset "UTF-8";
    @import url(http://fonts.googleapis.com/earlyaccess/notosanskr.css);
    @import url('https://media.vlpt.us/images/easycheaploansuk/post/e7865b20-64df-4117-9b73-d824d60bfe97/christmas.jpg');
    .container{
      padding-bottom: 0;
    }
    .itiscard{
      padding: 0%;
    }
    body {
        background: #f5f5f5;
        font-family: Roboto, sans-serif;
    }
    .blog .blog-thumbnail {
        background-size: cover;
        /* background-position: center center; */
        height: 100%;
        min-height: 300px;

    }
    .blog a:hover {
        opacity: 0.5;
        text-decoration: none;
    }
   
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
.boxbox {
  padding: 30px !important;
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
padding: 40px 30px;
}
.row1:nth-child(10),
.row1:nth-child(2),
.row1:nth-child(8) {
background: #134a46;
}
.row1:nth-child(3),
.row1:nth-child(7) {
background: #377d6a;
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

.h1font {
  color: white;
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
    color: #aaa;
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