<template>
  <div>
    <h1>커뮤니티</h1>
    <b-form-input type="text" v-model="search"></b-form-input> <b-button @click="searchTag">tag로 보기</b-button>
<table class="container">
  <thead>
      <tr>
        <th>
          <h1> No. </h1>
        </th>
        <th>
          <h1> 제목 </h1>
        </th>
        <th>
          <h1> 글쓴이 </h1>
        </th>
      </tr>
    </thead>
    <tbody>
  
    <community-item
      v-for="community in communities" 
      :key="community.id"
      :community ="community"
    ></community-item>

</tbody>
</table>
    <b-button @click="createCommunity">글쓰기</b-button>

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
        url: `http://127.0.0.1:8000/community/search/${this.search}`,
        headers: this.setToken(),
      })
      .then(res => {
        // console.log(res)
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
    @charset "UTF-8";
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);

    body {
        font-family: 'Open Sans', sans-serif;
        font-weight: 300;
        line-height: 1.42em;
        color: #A7A1AE;
        background-color: #1F2739 ;
    }

    h1 {
        font-size: 2em !;
        font-weight: 300;
        line-height: 1em;
        text-align: center;
        color: #fa4d4d ;
    }

    h2 {
        font-size: 1em;
        font-weight: 300;
        text-align: center;
        display: block;
        line-height: 1em;
        padding-bottom: 2em;
        color: #FB667A;
    }

    h2 a {
        font-weight: 700;
        text-transform: uppercase;
        color: #FB667A;
        text-decoration: none;
    }

    .blue {
        color: #185875;
    }
    .yellow {
        color: #FFF842;
    }

    .container th h1 {
        font-weight: bold;
        font-size: 1.3em;
        text-align: center;
        color: #185875;
    }

    .container td {
        font-weight: normal;
        font-size: 1em;
        -webkit-box-shadow: 0 2px 2px -2px #0E1119;
        -moz-box-shadow: 0 2px 2px -2px #0E1119;
        box-shadow: 0 2px 2px -2px #0E1119;
    }

    .container {
        text-align: center;
        overflow: hidden;
        width: 70%;
        margin: 0 auto;
        display: table;
        padding: 0 0 8em;
    }

    .container td,
    .container th {
        padding-bottom: 2%;
        padding-top: 2%;
        padding-left: 2%;
    }

 
    .container tr:nth-child(odd) {
        background-color: rgb(131, 18, 22);
    }

 
    .container tr:nth-child(even) {
        background-color: rgb(51, 77, 16);
    }

    .container th {
        background-color: black;
    }

    .container td:nth-child(odd) {
      font-size: 1.2em;
        color: #ccc7c7;
        font-weight: bold;
    }
    .container td:nth-child(even) {
      font-size: 1.2em;
        color: #ccc7c7;
        font-weight: bold;
    }


    .container tr:hover {
        background-color: #464A52;
        -webkit-box-shadow: 0 6px 6px -6px #0E1119;
        -moz-box-shadow: 0 6px 6px -6px #0E1119;
        box-shadow: 0 6px 6px -6px #0E1119;
    }

    .container td:hover {
        background-color: #FFF842;
        color: #403E10;
        font-weight: bold;

        box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
        transform: translate3d(6px, -6px, 0);

        transition-delay: 0s;
        transition-duration: 0.4s;
        transition-property: all;
        transition-timing-function: line;
    }

    @media (max-width: 800px) {
        .container td:nth-child(4),
        .container th:nth-child(4) {
            display: none;
        }
    }
</style>


