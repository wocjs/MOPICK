<template>
  <div>
    <br>
    <h3><span id=h3><i>{{ username }}</i>&nbsp;&nbsp;&nbsp;님을 위한 취향 저격 영화들</span></h3>
      <div class="cont" ref="imageContainer1">
          <div class="img-wrapper">
            <img
            v-for = "(movie, index) in simMovies"
            :key="index"
            :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
            class="movie-poster relimg"
            @click="toDetail(movie.id)"
            >
          </div>
      </div>
      <br><br>
      <button id="recoButton"
        class="movie-button btnhov"
        @click="toBase()"
      >
      새로 추천받기

      </button>
    </div>
</template>

<script>
import axios from 'axios'
const API_KEY = 'c376bdf28af008508b9156b102e6baf9'
export default {
  data(){
    return {
      likeMovies:null,
      simMovies:[],
      username: null,
    }
  },
  created(){
    this.getMyMovies()
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
    getMyMovies(){
      const token = this.$store.state.token;
      axios({
        method:'get',
        url:"http://127.0.0.1:8000/accs/getLikeMovie/",
        headers:{
          Authorization: `Token ${token}`
        }
      })
      .then((res)=>{
        // console.log(res)
        this.username = res.data.username
        const like_movie = res.data.like_movie
        this.likeMovies = like_movie.split(',')
        console.log(this.likeMovies[0] === "")
        if(this.likeMovies[0] === ""){
          alert("좋아하는 영화가 없습니다. 새로운 정보를 저장합니다.")
          this.$router.push({name:'BaseView'})
        }
        for(let likemovieid of this.likeMovies){
          let detMovAPI_URL = `https://api.themoviedb.org/3/movie/${likemovieid}?language=ko-KR`
          axios.get(detMovAPI_URL, {
            params: {
              api_key: API_KEY
            }
          })
          .then(response => {
            // console.log(response)
            console.log('##########')
            this.simMovies.push(response.data)
          })
        }
        // console.log(this.simMovies)
        for(let likemovieid of this.likeMovies){
          let simMovieAPI_URL = `https://api.themoviedb.org/3/movie/${likemovieid}/similar?api_key=c376bdf28af008508b9156b102e6baf9&language=ko-KR&page=1&certification_country=KR&certification.lte=15`
          axios({
            method:'get',
            url: simMovieAPI_URL
          })
          .then((rest)=>{
            const tmpLst = rest.data.results
            for (let simmov of tmpLst){
              const isDuplicate = this.simMovies.some(movie => movie.id === simmov.id);
              if(simmov.poster_path && simmov.popularity>20 && !isDuplicate){
                this.simMovies.push(simmov)
              }
              if(this.simMovies.length > 50){
                break
              }
            }
            this.simMovies = this.shuffleArray(this.simMovies)
          })
          .catch((errr)=>{
            console.log(errr)
          })
          let recMovieAPI_URL = `https://api.themoviedb.org/3/movie/${likemovieid}/recommendations?api_key=c376bdf28af008508b9156b102e6baf9&language=ko-KR&page=1&certification_country=KR&certification.lte=15`
          axios({
            method:'get',
            url: recMovieAPI_URL
          })
          .then((rest)=>{
            const tmpLst = rest.data.results
            for (let simmov of tmpLst){
              const isDuplicate = this.simMovies.some(movie => movie.id === simmov.id);
              if(simmov.poster_path && simmov.popularity>20 && !isDuplicate){
                this.simMovies.push(simmov)
              }
              if(this.simMovies.length > 50){
                break
              }
            }
            this.simMovies = this.shuffleArray(this.simMovies)
          })
          .catch((errr)=>{
            console.log(errr)
          })

        }
      })
      .catch((err)=>{
        console.log(err)
      })
      this.simMovies= this.shuffleArray(this.simMovies)
      setTimeout(()=>{
        console.log(this.simMovies)
      }, 500)
    },
    toDetail(id){
      // console.log(id)
      this.$router.push({name:"MovieDetailView", params:{"id":id}})
    },
    toBase(){
      this.$router.push({name:"BaseView"})
    }
  }
}
</script>

<style>

.movie-poster {
  opacity: 1;
  transition: opacity 0.1s ease-in-out;
  margin: 3px;
  width: 210px;
  height: 280px;
  border-radius: 20px;
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
  border: solid 4px;
}

/* img{
  margin: 3px;
  width: 210px;
  height: 280px;
  border-radius: 20px;
} */
.recthree{
  float: center;
  justify-content: center;
}
.img-wrapper{
  text-align: center;
}
.relimg:hover {
  transform: scale(1.15);
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
  /* 225*85 ==  */
  width: 250px;
  height: 95px;
  font-size: 33px;
}
</style>