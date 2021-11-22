import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/movies/Home.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieDetail from '@/views/movies/MovieDetail'
import MyPage from '@/views/accounts/MyPage'
import MyPageList from '@/views/accounts/MyPageList'
import Community from '@/views/community/Community'
import CommunityDetail from '@/views/community/CommunityDetail'
import CreateCommunity from '@/components/CreateCommunity'


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
  {
    path: '/accounts/mypagelist',
    name: 'MyPageList',
    component: MyPageList,
  },
  {
    path:'/community',
    name: 'Community',
    component: Community,

  },
  {
    path:'/community/:communityId',
    name: 'CommunityDetail',
    component: CommunityDetail,

  },
  {
    path:'/community/create',
    name: 'CreateCommunity',
    component: CreateCommunity,

  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
