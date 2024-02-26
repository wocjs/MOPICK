<template>
  <div id="app">
    <nav v-show="printt()" style="background-color: #000" class="navbar">
      <a id="leftGroup" href="http://localhost:8080/movie">
        <img src="@/assets/mopick.png" alt="MOPICK" />
      </a>
      <span id="centerGroup">
        <router-link :to="{ name: 'MovieView' }">Movies</router-link>
        <span class="divider">&nbsp;|&nbsp;</span>
        <router-link :to="{ name: 'ArticleView' }">Posts</router-link>
        <span class="divider">&nbsp;|&nbsp;</span>
        <router-link :to="{ name: 'RecoView' }">Recommends</router-link>
        <span class="divider">&nbsp;|&nbsp;</span>
        <router-link :to="{ name: 'SearchView' }">Search</router-link>
      </span>
      <span id="rightGroup">
        <router-link :to="{ name: 'LogInView' }" style="float: right"
          >LogOut</router-link
        >
        <span class="divider" style="float: right">&nbsp;|&nbsp;</span>
        <router-link :to="{ name: 'UpdateView' }" style="float: right"
          >회원 정보 수정</router-link
        >
      </span>
    </nav>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  data() {
    return {
      bgURL: null,
    };
  },
  created() {
    this.printt();
    // this.getBackgroundImage()
  },
  methods: {
    printt() {
      // console.log(this.$route.name)
      if (
        this.$route.name === "LogInView" ||
        this.$route.name === "SignUpView"
      ) {
        return false;
      }
      return true;
    },
    logout() {
      this.$store.dispatch("logout");
    },
    // shuffleArray(array) {
    //   const shuffledArray = array.slice(); // 원본 배열 복사
    //   let currentIndex = shuffledArray.length;

    //   while (currentIndex !== 0) {
    //     const randomIndex = Math.floor(Math.random() * currentIndex);
    //     currentIndex--;

    //     [shuffledArray[currentIndex], shuffledArray[randomIndex]] = [
    //       shuffledArray[randomIndex],
    //       shuffledArray[currentIndex],
    //     ];
    //   }
    //   return shuffledArray
    // },
    // getBackgroundImage(){
    //   const djangoURL = "http://127.0.0.1:8000/movies/getmovies/"
    //   axios({
    //     method:'get',
    //     url:djangoURL
    //   })
    //   .then((res)=>{
    //     const tmpLst = res.data
    //     this.baseMovies = this.shuffleArray(tmpLst)
    //     const randMovId = this.baseMovies[0].movie_id
    //     const tmdbURL = `https://api.themoviedb.org/3/movie/${randMovId}?language=ko-KR`
    //     axios.get(tmdbURL, {
    //       params:{
    //         api_key : `c376bdf28af008508b9156b102e6baf9`
    //       }
    //     })
    //     .then((res)=>{
    //       const bdpath = res.data.backdrop_path
    //       console.log(bdpath)
    //       this.bgURL = `https://image.tmdb.org/t/p/w500/${bdpath}`
    //       return `https://image.tmdb.org/t/p/original/${bdpath}`
    //     })
    //   })
    //   .catch((err)=>{
    //     console.log(err)
    //     alert("에러 발생!!!")
    //   })
    // }
  },
};
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #ffffff;
}

/* nav {
  padding: 15px;
} */

nav a {
  font-weight: bold;
  font-size: larger;
  color: #666666;
  white-space: nowrap;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #fff;
}

span {
  color: #666666;
}

#centerGroup {
  display: flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  flex-wrap: nowrap;
}

#leftGroup {
  display: inline-block;
  margin-right: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
}

#rightGroup {
  display: inline-block;
  margin-left: 10px;
  margin-right: 10px;
}

#centerGroup > * {
  margin-right: 10px;
}

#rightGroup > * {
  margin-left: 10px;
}

.navbar {
  font-family: omu_allpretty;
  font-size: 20px;
}
</style>
