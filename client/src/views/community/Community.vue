<template>
  <div>
    <h1>커뮤니티</h1>
    <input type="text" v-model="search"> <button @click="searchTag">tag로 보기</button>
    <community-item
      v-for="community in communities" 
      :key="community.id"
      :community ="community"
    ></community-item>
    <button @click="createCommunity">글쓰기</button>

  </div>
</template>

<script>
import axios from 'axios'
import CommunityItem from '@/components/CommunityItem.vue'

export default {
  components: { CommunityItem },
  name: 'Community',
  data: function () {
    return {
      communities: null,
      search: null,
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
    searchTag: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.search}`,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        this.communities = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    getCommunities: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.setToken(), // Authorization: JWT token값
      })
        .then(res => {
          this.communities = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createCommunity: function() {
      this.$router.push({name: 'CreateCommunity'})
    },
    },
  created: function () {
    if (localStorage.getItem('jwt')){
        this.getCommunities()
    }
    else{
      this.$router.push({name: 'Login'})
    }
    
  }
}
</script>

<style>

</style>


