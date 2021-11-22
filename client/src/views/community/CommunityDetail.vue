<template>
  <div>
    <h1>CommunityDetail</h1>

    {{community.id}}
    <br>
    {{community.title}}
    <br>
    {{community.content}}
    <br>
    {{community.created_at}}
    <br>
    {{community.updated_at}}
    <br>
    {{username}}
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

<style>

</style>