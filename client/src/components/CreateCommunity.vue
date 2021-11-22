<template>
  <div>
    제목: <input type="text" v-model="title">
    <br>
    내용: <input type="text" v-model="content">
    <br>
    <button @click="createCommunity">Submit</button>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateCommunity',
  data: function() {
    return {
      title: null,
      content: null,
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

    createCommunity: function () {
      const communityItem = {
        title: this.title,
        content : this.content
      }

      if (communityItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/community/',
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
      }
    }
}

}
</script>

<style>

</style>