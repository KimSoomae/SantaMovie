import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/movies/Home.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieDetail from '@/views/movies/MovieDetail'
import ChristmasMovieDetail from '@/views/movies/ChristmasMovieDetail'
import MyPage from '@/views/accounts/MyPage'
import MyPageList from '@/views/accounts/MyPageList'
import Community from '@/views/community/Community'
import CommunityDetail from '@/views/community/CommunityDetail'
import CreateCommunity from '@/components/CreateCommunity'
import UpdateCommunity from '@/components/UpdateCommunity'
import Test from '@/views/Test'
import Test2 from '@/views/movies/test'


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
    path: '/christmasmovie/:christmasmovieId',
    name: 'ChristmasMovieDetail',
    component: ChristmasMovieDetail
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

  {
    path:'/community/update/:communityId',
    name: 'UpdateCommunity',
    component: UpdateCommunity,

  },

  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
