import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/movies/Home.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieDetail from '@/views/movies/MovieDetail'
import MyPage from '@/views/accounts/MyPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/movie/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },

  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/mypage',
    name: 'MyPage',
    component: MyPage,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
