import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import ArticleCreateView from '@/views/ArticleCreateView'
import ArticleDetailView from '@/views/ArticleDetailView'
import ArticleUpdateView from '@/views/ArticleUpdateView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import BaseView from '@/views/BaseView'
import MovieView from '@/views/MovieView'
import MovieDetailView from '@/views/MovieDetailView'
import SearchView from '@/views/SearchView'
import UpdateView from '@/views/UpdateView'
import ProfileView from '@/views/ProfileView'
import RecoView from '@/views/RecoView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView,
  },
 
  {
    path: '/article/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView,
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
  },

  {
    path: '/',
    name: 'LogInView',
    component: LogInView,
  },

  {
    path: '/article/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
  },

  {
    path: '/article/:id/update',
    name: 'ArticleUpdateView',
    component: ArticleUpdateView,
  },
  
  {
    path: '/base',
    name: 'BaseView',
    component: BaseView,
  },
  {
    path: '/movie',
    name: 'MovieView',
    component: MovieView,
  },
  {
    path: "/movie/:id",
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView,
  },
  {
    path: '/update',
    name: 'UpdateView',
    component: UpdateView,
  },
  {
    path: '/profile/:id',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/reco',
    name: 'RecoView',
    component: RecoView,
  },
]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  // console.log('to', to)
  // console.log('from', from)
  const loggedIn = localStorage.getItem('vuex')
  // console.log(loggedIn)
  // 로그인이 필요한 페이지인 경우
  const freePages = ['LogInView', 'SignUpView']
  const authRequired = !freePages.includes(to.name) //true면 필요한 경우
  // console.log(authRequired)
  if(!loggedIn && authRequired){
    // 로그인 체크 하고
    // console.log('first')
    alert('로그인이 필요한 서비스 입니다!')
    next({name:'LogInView'})
  }
  else{
    // console.log('second')
    next()
  }
})
export default router
