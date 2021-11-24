<template>
<div>
  <div class="blog py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-8 mx-auto px-0 bg-white shadow-sm rounded itiscard">
          <div class="col-lg-5 col-md-12 float-md-left blog-thumbnail" style="background-image: url('https://media.vlpt.us/images/easycheaploansuk/post/e7865b20-64df-4117-9b73-d824d60bfe97/christmas.jpg')"></div>
          <div class="col-lg-7 col-md-12 float-md-left">
            <div class="p-3 p-sm-5">
              <div class="mb-4">
                <h3 class="mb-4">
                  {{community.title}}
                </h3>
                <div class="mb-0">
                <p>{{community.content}}</p>
                <hr>
                Time: {{community.updated_at}}
                <br>
                글쓴이: {{username}}
                </div>
                <br>
                <div>
                <span class="text-success" v-for="tag in community.tags" :key="tag.id">#{{tag.name}} </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="row1">
  <span>
    <input class="balloon" id="state" type="text" placeholder="댓글을 작성하세요." /><label for="state">Comment</label>
  </span>
  
</div>
   <comment-list :comments="community.comments"></comment-list>
    <create-comment :community ="community.id"></create-comment>
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
         
          const content = {
            token: this.setToken(),
            userid: this.community.user
          }
          this.$store.dispatch('GetUserName', content)
        })
        .catch(err => {
          console.log(err)
        })
        
    },
  },
  computed: {
    ...mapState(['username'])
  },
  created: function () {
    if (localStorage.getItem('jwt')){
        this.getCommunityDetail()
    }
    else{
      this.$router.push({name: 'Login'})
    }
    
  }
}
</script>

<style scoped>
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
        background-position: center center;
        height: 350px;
        /* min-height: 300px; */
        /* position: absolute */
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
    font-family: "Open Sans", sans-serif;
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

}
.row1:before {
position: absolute;
content: "";
display: block;
top: 0;
left: -5000px;
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