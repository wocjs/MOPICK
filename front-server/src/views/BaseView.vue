<template>
  <div>
    <br>
    <h3 style="text-align:center;font-"><span id="h3">선호하는 영화를 3가지 이상 선택해 주세요!</span></h3>
    <br>
    <div class="cont" ref="imageContainer1">
        <div class="img-wrapper">
          <img
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          :alt="movie.title"
          class="movie-poster"
          v-for = "(movie, index) in baseMovies"
          :key="index"
          @click="updateMyMovie(movie.movie_id)"
          :class="{'selected':selectedMovies.includes(movie.movie_id)}"
          >
        </div>
    </div>
    <br><br>
    <button
      class="movie-button btnhov"
      :class="{'active': selectedMovies.length >= 3}"
      :disabled="selectedMovies.length < 3"
      @click="navigateToMovieView"
      id="recoButton"
    >
    선택 완료!
    </button>
  </div>
</template>

<script>
// import { gsap } from 'gsap';
import axios from 'axios'
export default {
  name:'BaseView',
  data(){
    return{
      baseMovies:null,
      selectedMovies:[]
    }
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  created(){
    this.getMovieFromDB()
  },
  methods:{
    shuffleArray(array) {
      const shuffledArray = array.slice(); // 원본 배열 복사
      let currentIndex = shuffledArray.length;

      while (currentIndex !== 0) {
        const randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [shuffledArray[currentIndex], shuffledArray[randomIndex]] = [
          shuffledArray[randomIndex],
          shuffledArray[currentIndex],
        ];
      }
      return shuffledArray
    },
    getMovieFromDB(){
      if(this.isLogin){
        // console.log('로그인은 되어있음')
        const URL = "http://127.0.0.1:8000/movies/getmovies/"
        axios({
          method:'get',
          url:URL
        })
        .then((res)=>{
          const tmpLst = res.data
          this.baseMovies = this.shuffleArray(tmpLst)
        })
        .catch((err)=>{
          console.log(err)
          alert("에러 발생!!!")
        })
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name:'LogInView'})
      }
    },
    updateMyMovie(title){
      if (this.selectedMovies.includes(title)){
        const index = this.selectedMovies.indexOf(title)
        this.selectedMovies.splice(index, 1)
      }
      else{
        this.selectedMovies.push(title)
      }
    },
    navigateToMovieView(){
      const token = this.$store.state.token;
      const selectedMovies = this.selectedMovies.join(',')
      axios({
        method:'post',
        url: "http://127.0.0.1:8000/accs/getLikeMovie/",
        data: { "like_movie":selectedMovies },
        headers:{
          Authorization: `Token ${token}`
        }
      })
      this.$router.push({name:"MovieView"})
    }
  }
}
</script>

<style scoped>
/* img{
  padding:10px;
  width: 210px;
  height: 280px;
} */
.movie-poster {
  opacity: 1;
  transition: opacity 0.1s ease-in-out;
}

.movie-poster.selected {
  opacity: 0.3;
}

.movie-button {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  border-radius: 20px;
  font-weight: bold;
  font-size:30px;
  cursor: pointer;
  /* opacity: 0.5; */
  transition: opacity 0.3s ease-in-out;
  background-color: #ffffff;
  color:rgb(225, 29, 37);
  font-family: omu_allpretty;
  font-weight: lighter;
  font-size: 38px;
  border: solid 4px;
}

.movie-button:disabled {
  color:rgb(10, 10, 10);
  background-color: #5f5f5f;
}
img{
  /* display: inline-block; 이미지들이 가로로 나열되도록 설정 */
  margin: 3px;
  width: 210px;
  height: 280px;
  border-radius: 20px;
}
.recthree{
  float: center;
  justify-content: center;
}
.img-wrapper{
  text-align: center;
}

#h3 {
  font-family: omu_allpretty;
  font-weight: bold;
  font-size: 38px;
}

#recoButton {
  font-family: omu_allpretty;
  font-weight: lighter;
  font-size: 38px;
}

.btnhov:hover{
  /* 175.5*85 ==  */
  width: 190px;
  height: 95px;
  font-size: 33px;
}
</style>