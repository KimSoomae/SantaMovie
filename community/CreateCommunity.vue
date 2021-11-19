<template>
  <div>
    <h1>Write Form</h1>
    <input 
      type="text" 
      v-model.trim="title" 
    >
    <input 
      type="text" 
      v-model.trim="content" 
    >
    <input
    type="text"
    v-model.trim="tags"
    >
    <!-- <ul>
      <li v-for="tag in tags" :key="todo.id">
        <span @click="updateTodoStatus(todo)" :class="{ 'is-completed': todo.is_completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
       -->
    <button @click="createCommunity">+</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateCommunity',
  data: function(){
    return{
      title: null,
      content: null,
      tags: [],
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
    createCommunity: function() {
      const community = {
        title: this.title,
        content: this.content,
        tags: this.tags,
      }

      axios({
        method: 'post',
          url: 'http://127.0.0.1:8000/community/community_create/',
          data: community,
          headers: this.setToken(),
      })
      .then(res => {
        this.$router.push({name: 'Community'})
        console.log(res)
      })
      
    }
  }
}
</script>

<style>

</style>