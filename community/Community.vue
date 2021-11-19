<template>
  <div>
    <h1>커뮤니티</h1>
    <ul>
      <li v-for="community in communities" :key="community.id">
        <span>{{ community.title }}</span>
        <span>{{community.tags.name}} </span>
      </li>
    </ul>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  data: function () {
    return {
      communities: null,
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
    getCommunities: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/community_create/',
        headers: this.setToken(), // Authorization: JWT token값
      })
        .then(res => {
          console.log(res)
          this.communities = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    // deleteTodo: function (todo) {
    //   axios({
    //     method: 'delete',
    //     url: `http://127.0.0.1:8000/todos/${todo.id}/`,
    //     headers: this.setToken(),
    //   })
    //     .then(res => {
    //       console.log(res)
    //       this.getTodos()
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },
    // updateTodoStatus: function (todo) {
    //   const todoItem = {
    //     ...todo,
    //     is_completed: !todo.is_completed
    //   }

    //   axios({
    //     method: 'put',
    //     url: `http://127.0.0.1:8000/todos/${todo.id}/`,
    //     data: todoItem,
    //     headers: this.setToken(),
    //   })
    //     .then(res => {
    //       console.log(res)
    //       todo.is_completed = !todo.is_completed
    //     })
    //   },
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

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
