<template>
  
  <v-app>
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->
    <Snow/>
   
    <div id="app">
    <div id="nav">
     
      <router-link to="/">
        <v-img src="@/assets/SantaMovieLogo.png" :to="{name: 'Home' }" style="display: inline-block; float:left; margin-top:-40px;width: 100px; height: 100px; vertical-align: middle; " >
        </v-img>
      </router-link>
      
      <span v-if="isLogin">
        <span style="margin-left: 200px;">
          <router-link to="/">Home</router-link> |
          <router-link @click.native="logout" to="#">Logout</router-link> |
          <router-link :to="{ name: 'MyPageList' }">MyPage</router-link> |
          <router-link :to="{ name: 'Community' }">Community</router-link> |
        </span>
   
      </span>
      <span v-else>
        <span style="margin-left: 200px;">
          <router-link :to="{ name: 'Signup' }">Signup</router-link> |
          <router-link :to="{ name: 'Login' }">Login</router-link> 
        </span>
      </span>
    <audio autoplay controls loop>
      <source src="@/audio/Mariah Carey-02-All I Want for Christmas Is You-Merry Christmas.mp3" type="audio/mpeg"> 브라우저가 audio 태그를 지원하지 않을 때 표시되는 문장
    </audio>
    </div>
    <router-view @login="isLogin = true"/>
    <v-footer v-if="isLogin" padless dark>
    <v-col
      class="py-2 white--text text-center"
      cols="12"
    >
      {{ new Date().getFullYear() }}.11 - <strong>Coding Soojae</strong><br>
      Jaehyeon Ko <v-icon size="24px">
            {{ icon }}
          </v-icon> jjjhyeon._.v <br>
      Soomin Kim <v-icon size="24px">
            {{ icon }}
          </v-icon> so_omae
    </v-col>
  </v-footer>
  </div>
  </v-app>

</template>

<script>
import Snow from 'vue-niege';
// import Snowf from 'vue-snowf';
export default {
  name: 'App',
  components: {
    Snow
      // Snowf
  },
  data: function() {
    return{
      icon: 'mdi-instagram',
      isLogin:false,
    }
  },
  methods: {
    logout: function() {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({name: 'Login'})
    }

  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    } else {
      this.$router.push({name: 'Login'})
    }
  }
};

</script>
<style >
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Gowun+Dodum&family=Poor+Story&display=swap');

audio {
  color: red;
  display: inline;
  float: right;
  margin: -15px auto;
}
  #app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgb(66, 47, 30);
} 

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #ccc7c7;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
