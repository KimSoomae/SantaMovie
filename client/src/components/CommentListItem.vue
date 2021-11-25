<template>
  <div class="comment">
    {{comment.id}}.
    {{comment.title}}
  
    <span class="smallusername">
    by {{username}}
    </span>
    <!-- {{comment.created_at}}
    {{comment.updated_at}} -->
    
    <!-- <b-button @click="deleteComment">삭제</b-button> -->
    <v-btn
              color="error"
              fab
              x-small
              dark
              @click="deleteComment"
              style="text-align:center;"
              class="btnbtn"
            >
              <v-icon>X</v-icon>
            </v-btn>
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

<style scoped>
.smallusername {
    font-size: 70% ;
  }
  .comment {
    color: #ccc7c7;
    font-size: 150%;
    margin-bottom: 10px;
    
  }

  

</style>