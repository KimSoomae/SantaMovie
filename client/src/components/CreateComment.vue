<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
    >
    <button @click="createComment">+</button>

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

</style>





