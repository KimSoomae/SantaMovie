<template>
  
  <v-app>
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->
    <Snow/>
    <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <router-link to="/">Home</router-link> |
        <router-link @click.native="logout" to="#">Logout</router-link> |
        <router-link :to="{ name: 'MyPageList' }">MyPage</router-link> |
        <router-link :to="{ name: 'Community' }">Community</router-link> |
   
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="isLogin = true"/>
  </div>
  </v-app>
  <!-- <v-app>
    
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
      
         -->
    <!-- <router-view @login="isLogin = true"/>
        <div id="nav">
          <span v-if="isLogin">
            <router-link to="/">Home</router-link> |
            <router-link @click.native="logout" to="#">Logout</router-link> |
            <router-link :to="{ name: 'MyPageList' }">MyPage</router-link> |
            <router-link :to="{ name: 'Community' }">Community</router-link> 
          </span>
          <span v-else>
            <router-link :to="{ name: 'Signup' }">Signup</router-link> |
            <router-link :to="{ name: 'Login' }">Login</router-link> 
          </span>
       </div>
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app> -->
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
  #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
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
