<template>
  <div @click="goToCommunityDetail">
    {{community.id}} ---- {{community.title}} ----- {{username}}
  </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
  name: 'CommnunityItem',
  props: {
    community : {
      type: Object
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
    goToCommunityDetail: function() {
      this.$router.push({name: 'CommunityDetail', params: {communityId: this.community.id}})
    },
    getUserName: function() {
      const content = {
            token: this.setToken(),
            userid: this.community.user
          }
          this.$store.dispatch('GetUserName', content)
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')){
        this.getUserName()
    }
    else{
      this.$router.push({name: 'Login'})
    }
    
  },
  computed: {
    ...mapState(['username'])
  },
    
  }


</script>

<style>

</style>