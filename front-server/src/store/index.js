import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedstate from 'vuex-persistedstate'
import router from '../router'


const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedstate(),
  ],

  state: {
    articles: [
    ],
    token: null,
    isLiked: false,
    commentLikes: [

    ],
  },
  getters: {
    getIsLiked(state) {
      return state.isLiked
    },
    getIsCommentLiked(state) {
      return (commentId) => {
        return state.isCommentLiked[commentId] || false
      }
    },
    isLogin(state){
      return state.token ? true : false
    },
    getCommentLikes: (state) => state.commentLikes,
    isCommentLiked: (state) => (commentId) => {
      return state.commentLikes.includes(commentId)
    },
  },
  mutations: {
    SET_COMMENT_LIKES(state, commentLikes) {
      state.commentLikes = commentLikes
    },
    TOGGLE_COMMENT_LIKE(state, commentId) {
      const index = state.commentLikes.indexOf(commentId)
      if (index > -1) {
        state.commentLikes.splice(index, 1)
      } else {
        state.commentLikes.push(commentId)
      }
    },
    update_IsLiked(state, value) {
      state.isLiked = value
    },
    updateCommentLiked(state, payload) {
      state.isCommentLiked[payload.commentId] = payload.isLiked
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // signUp & login : 완료하면 토큰 발급 == 이를 사용해 로그인 가능
    SAVE_TOKEN(state, token){
      state.token = token
      axios({
        method:'get',
        url:"http://127.0.0.1:8000/accs/getLikeMovie/",
        headers:{
          Authorization: `Token ${token}`
        }
      })
      .then((res)=>{
        // console.log('#######################')
        // console.log(res)
        // console.log('#######################')
        if(res.data.like_movie){
          router.push({name:'MovieView'}).catch(()=>{}) // store/index.js $router 접근 불가 -> import 해줘야함
        }
        else{
          router.push({name:'BaseView'}).catch(()=>{}) // store/index.js $router 접근 불가 -> import 해줘야함
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    CHANGE_LIKE(state){
      state.isLiked = !state.isLiked
    },
    DELETE_TOKEN(state){
      state.token = null
      state.articles = []
      localStorage.removeItem('vuex');
      localStorage.removeItem('token'); // localStorage에서 'token' 항목을 제거
      // router.push({name:'LoginView'}).catch(()=>{})
    }
    // CREATE_COMMENT(state, commentItem) {
    //   state.todos.push(commentItem)
    //   console.log(state.comments)
    // }
  },
  beforeRouteUpdate(to, from, next){
    console.log('to, from')
    console.log(to, from)
    // console.log('to.params.id', to.params.id)
    // this.isLiked = to.params.
    next()
  },
  actions: {
    updateIsLiked({ commit }, value) {
      commit('update_IsLiked', value)
    },
    updateCommentLiked({ commit, state }, payload) {
      const commentId = payload.commentId
      const isLiked = payload.isLiked

      if (state.isCommentLiked[commentId] !== undefined) {
        // 댓글에 이미 좋아요가 존재하는경우 업데이트
        commit('updateCommentLiked', payload)
      } else {
        // 댓글에 좋아요 없으면 추가
        state.isCommentLiked[commentId] = isLiked
      }
    },
    changeLike({commit}){
      commit('CHANGE_LIKE')
    },
    setCommentLikes({ commit }, commentLikes) {
      commit('SET_COMMENT_LIKES', commentLikes)
    },
    // toggleCommentLike({ commit, state }, commentId) {
    //   commit('TOGGLE_COMMENT_LIKE', commentId)
    // },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload){
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method:'post',
        url: `${API_URL}/accounts/signup/`,
        data :{
          username, password1, password2
        }
      })
      .then((res)=>{
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        alert('이미 있는 아이디 입니다')
        console.log(err)
      })
    },
    login(context, payload){
      const username = payload.username
      const password = payload.password
      axios({
        method:'post',
        url: `${API_URL}/accounts/login/`,
        data:{
          username, password
        }
      })
      .then((res)=>{
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(()=>{
        alert('아이디 또는 비밀번호를 확인해주세요!')
        // console.log(err)
      })
    },
    logout(context){
      context.commit('DELETE_TOKEN')
    }
  },
  modules: {
  }
})
