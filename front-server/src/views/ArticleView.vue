<template>
  <div>
    <br><br>
    <h1 id=Board_title>자유 게시판</h1>
    <div id="Create_post">
    <router-link :to="{ name: 'ArticleCreateView' }" style="color:whitesmoke">새 글 작성하기</router-link>
    </div>
    <hr>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'
// import LogInViewVue from './LogInView.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin // 로그인 여부 -> true 또는 false
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if(this.isLogin){
        this.$store.dispatch('getArticles')
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name:'LogInView'})
      }
      // 로그인 되어있으면 getArticles action 실행
      // 로그인 X : login 페이지로 이동
    }
  }
}
</script>

<style scoped>
#Board_title {
  text-align: center;
  font-weight: bold;
  font-family: omu_allpretty;
  font-size: 45px;
}
@font-face {
  font-family: 'establish Retrosans';
  src: url(@/fonts/establish_Retrosans.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}

a {
  text-decoration: none;
}

#Create_post {
  text-align: right;  
  font-family: omu_allpretty;
  /* font-weight: bold; */
  font-size: 23px;
  /* text-decoration-color: black; */
}

hr {
  border-width: 10px;
}
</style>
