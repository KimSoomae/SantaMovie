<template>
    <div id="form-main">
  <div id="form-div">
    <form class="form" id="form1">
      
      <p class="name">
        <input name="name" type="text" class="validate[required,custom[onlyLetter],length[0,100]] feedback-input" id="name" v-model="title"/> 
      </p>
      
      <p class="email">
        <input name="email" type="text" class="validate[required,custom[email]] feedback-input" id="email" placeholder="태그 앞에 #을 넣어주세요! 예시)#리뷰#추천#영화" v-model="tags"/>
      </p>
      
      <p class="text">
        <textarea name="text" class="validate[required,length[6,300]] feedback-input" id="comment" v-model="content"></textarea>
      </p>
      
      
      <div class="submit">
        <input value="SEND" id="button-blue" @click="updateCommunity"/>
        <div class="ease"></div>
      </div>
    </form>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateCommunity',
  data: function() {
    return {
      community: Object,
      title: null,
      content: null,
      tags: '',
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
        method: 'GET',
        url: `http://127.0.0.1:8000/community/${this.$route.params.communityId}`,
        headers: this.setToken(), // Authorization: JWT token값
      })
        .then(res => {
          // console.log(res)
          this.community = res.data
          this.title = this.community.title
          this.content = this.community.content
          for(var v of this.community.tags) {
            this.tags += ('#'+v.name )
          }
        })
        .catch(err => {
          console.log(err)
        })
        
    },

    updateCommunity: function () {
      const communityItem = {
        title: this.title,
        content : this.content,
        tags: this.tags,
      }

      if (communityItem.title) {
        axios({
          method: 'PUT',
          url: `http://127.0.0.1:8000/community/${this.community.id}/`,
          data: communityItem,
          headers: this.setToken(),
        })
          .then(res => {
            
            this.$router.push({name: 'CommunityDetail', params: {communityId: res.data.id}})
          })
          .catch(err => {
            console.log(err)
          })
        this.title = null
        this.content = null
        this.tags = null
      }
    }
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


@import url(https://fonts.googleapis.com/css?family=Montserrat:400,700);


html{    
  background:url(http://thekitemap.com/images/feedback-img.jpg) no-repeat !important;
  background-size: cover;
  height:100%;
}

#feedback-page{
	text-align:center;
}

#form-main{
	width:100%;
	float:left;
	padding-top:0px;
}

#form-div {
	background-color:rgb(51, 77, 16);;
	padding-left:35px;
	padding-right:35px;
	padding-top:35px;
	padding-bottom:50px;
	width: 800px;
	float: left;
	left: 40%;
	position: absolute;
  margin-top:30px;
	margin-left: -260px;
  -moz-border-radius: 7px;
  -webkit-border-radius: 7px;
}

.feedback-input {
	color:#3c3c3c;
	font-family: Helvetica, Arial, sans-serif;
  font-weight:500;
	font-size: 18px;
	border-radius: 0;
	line-height: 22px;
	background-color: #fbfbfb;
	padding: 13px 13px 13px 54px;
	margin-bottom: 10px;
	width:100%;
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	-ms-box-sizing: border-box;
	box-sizing: border-box;
  border: 3px solid rgba(0,0,0,0);
}

.feedback-input:focus{
	background: #fff;
	box-shadow: 0;
	border: 3px solid #3498db;
	color: black;
	outline: none;
  padding: 13px 13px 13px 54px;
}

.focused{
	color:#30aed6;
	border:#30aed6 solid 3px;
}

/* Icons ---------------------------------- */
#name{
	background-image: url(http://rexkirby.com/kirbyandson/images/name.svg);
	background-size: 30px 30px;
	background-position: 11px 8px;
	background-repeat: no-repeat;
}

#name:focus{
	background-image: url(http://rexkirby.com/kirbyandson/images/name.svg);
	background-size: 30px 30px;
	background-position: 8px 5px;
  background-position: 11px 8px;
	background-repeat: no-repeat;
}

#email{
	/* background-image: url(http://rexkirby.com/kirbyandson/images/email.svg); */
	background-size: 30px 30px;
	background-position: 11px 8px;
	background-repeat: no-repeat;
}

#email:focus{
	/* background-image: url(http://rexkirby.com/kirbyandson/images/email.svg); */
	background-size: 30px 30px;
  background-position: 11px 8px;
	background-repeat: no-repeat;
}

#comment{
	/* background-image: url(http://rexkirby.com/kirbyandson/images/comment.svg); */
	background-size: 30px 30px;
	background-position: 11px 8px;
	background-repeat: no-repeat;
}

textarea {
    width: 100%;
    height: 150px;
    line-height: 150%;
    resize:vertical;
}

input:hover, textarea:hover,
input:focus, textarea:focus {
	background-color:white;

}

#button-blue{
	font-family: 'Montserrat', Arial, Helvetica, sans-serif;
	float:left;
	width: 100%;
	border: #fbfbfb solid 4px;
	cursor:pointer;
	background-color: rgb(131, 18, 22);;
	color:white;
	font-size:24px;
	padding-top:22px;
	padding-bottom:22px;
	-webkit-transition: all 0.3s;
	-moz-transition: all 0.3s;
	transition: all 0.3s;
  margin-top:-4px;
  font-weight:700;
  text-align: center;
}

#button-blue:hover{
	background-color: rgba(0,0,0,0);
	color: #0493bd;
}
	
.submit:hover {
	color: #3498db;
}
	
.ease {
	width: 0px;
	height: 74px;
	background-color: #fbfbfb;
	-webkit-transition: .3s ease;
	-moz-transition: .3s ease;
	-o-transition: .3s ease;
	-ms-transition: .3s ease;
	transition: .3s ease;
}

.submit:hover .ease{
  width:100%;
  background-color:white;
}

@media only screen and (max-width: 580px) {
	#form-div{
		left: 3%;
		margin-right: 3%;
		width: 88%;
		margin-left: 0;
		padding-left: 3%;
		padding-right: 3%;
	}
}

</style>