<template>
  <div>
    {{comment.id}}
    {{comment.title}}
    {{username}}
    <!-- {{comment.created_at}}
    {{comment.updated_at}} -->
    
    <button @click="deleteComment">삭제</button>
    <!-- modal -->
    
  </div>
</template>

<script>
import axios from 'axios'
import {mapState} from 'vuex'
export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
    communityid: Number,
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getUserName: function() {
      const content = {
            token: this.setToken(),
            userid: this.comment.user
          }
          this.$store.dispatch('GetUserName', content)
    },
    
    deleteComment: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/comment/${this.comment.id}/`,
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res)
          this.$router.go(this.$router.currentRoute)
          })
          .catch(err => {
            console.log(err)
          })
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