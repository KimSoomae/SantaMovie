<template>
  <div>
    제목: <input type="text" v-model="title">
    <br>
    내용: <input type="text" v-model="content">
    <br>
    태그 앞에 #을 넣어주세요
    태그: <input type="text" v-model="tags">
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
      tags: null,
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
        content : this.content,
        tags: this.tags,
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
        this.tags = null
      }
    }
}

}
</script>

<style>

</style>