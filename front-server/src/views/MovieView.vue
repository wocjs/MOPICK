<template><!--테스트2차-->
  <div>
    <br>
    <div v-if="simMovies.length">
      <h3>
        <span id="h3"><i>{{ username }}</i>&nbsp;&nbsp;&nbsp;님을 위한 취향 저격 영화들</span>
        <div style="float:right">
          <button @click="scrollLeft3()" :disabled="isScrollLeftEnd3" id="scrollLeftBtn3"><span class="bttn">&nbsp;&lt;&nbsp;</span></button>
          &nbsp;&nbsp;&nbsp;
          <button @click="scrollRight3()" :disabled="isScrollRightEnd3" id="scrollRightBtn3"><span class="bttn">&nbsp;&gt;&nbsp;</span></button>
          &nbsp;&nbsp;&nbsp;
        </div>
      </h3>
      <br>
      <div class="cont " ref="imageContainer3">
        <img class="img-fluid" @click="toDetail(movie.id)" v-for="(movie, index) in simMovies" :key="index" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
      </div>
      <br><br><br>
    </div>

    <h3>
      <span id="h3">죽기전에 꼭 봐야할 영화</span>
      <div style="float:right">
        <button @click="scrollLeft1()" :disabled="isScrollLeftEnd1" id="scrollLeftBtn1"><span class="bttn">&nbsp;&lt;&nbsp;</span></button>
        &nbsp;&nbsp;&nbsp;
        <button @click="scrollRight1()" :disabled="isScrollRightEnd1" id="scrollRightBtn1"><span class="bttn">&nbsp;&gt;&nbsp;</span></button>
        &nbsp;&nbsp;&nbsp;
      </div>
    </h3>
    <br>
    <div class="cont" ref="imageContainer1">
      <img @click="toDetail(movie.id)" v-for="(movie, index) in topMovies" :key="index" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
    </div>
    <br><br><br>
    
    <h3>
      <span id="h3">실시간 영화 순위</span>
      <div style="float:right">
        <button @click="scrollLeft2()" :disabled="isScrollLeftEnd2" id="scrollLeftBtn2"><span class="bttn">&nbsp;&lt;&nbsp;</span></button>
        &nbsp;&nbsp;&nbsp;
        <button @click="scrollRight2()" :disabled="isScrollRightEnd2" id="scrollRightBtn2"><span class="bttn">&nbsp;&gt;&nbsp;</span></button>
        &nbsp;&nbsp;&nbsp;
      </div>
    </h3>
    <br>
    <div class="cont" ref="imageContainer2">
      <img @click="toDetail(movie.id)" v-for="(movie, index) in popMovies" :key="index" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
    </div>
    <br><br><br><br>
  </div>
</template>

<script>
import axios from 'axios'
import { gsap } from 'gsap';
const API_KEY = 'c376bdf28af008508b9156b102e6baf9'
const topMovieAPI_URL = `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR&page=1&certification_country=KR&certification.lte=15`
const popMovieAPI_URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=ko-KR&page=1&certification_country=KR&certification.lte=15`
export default {
  name: 'MovieView',
  data(){
    return {
      topMovies: null,
      popMovies: null,
      currentTime: null,
      likeMovies:null,
      simMovies:[],
      username: null,
      isScrollLeftEnd1: false,
      isScrollRightEnd1: false,
      isScrollLeftEnd2: false,
      isScrollRightEnd2: false,
      isScrollLeftEnd3: false,
      isScrollRightEnd3: false
    }
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  created(){
    this.getTopMovies()
    this.getPopMovies()
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
    getTopMovies(){
      if(this.isLogin){
        axios({
          method:'get',
          url: topMovieAPI_URL
        })
        .then((res)=>{
          const tmpLst = res.data.results.filter(movie => movie.adult === false);
          this.topMovies = this.shuffleArray(tmpLst)
          setTimeout(()=>{
            this.updateScrollButtonState1();
          }, 200)
        })
        .catch((err) => {
          console.log(err)
        })
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name:'LogInView'})
      }
    },
    getPopMovies(){
      axios({
        method:'get',
        url: popMovieAPI_URL
      })
      .then((res)=>{
        this.popMovies = res.data.results
        setTimeout(()=>{
          this.updateScrollButtonState2();
        }, 200)
      })
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
        for(let likemovieid of this.likeMovies){
          let detMovAPI_URL = `https://api.themoviedb.org/3/movie/${likemovieid}?language=ko-KR`
          axios.get(detMovAPI_URL, {
            params: {
              api_key: API_KEY
            }
          })
          .then(response => {
            // console.log(response)
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
          
        }
        setTimeout(()=>{
          this.updateScrollButtonState3();
        }, 500)
      })
      .catch((err)=>{
        console.log(err)
      })
      this.simMovies= this.shuffleArray(this.simMovies)
      console.log(this.simMovies)
    },
    toDetail(id){
      // console.log(id)
      this.$router.push({name:"MovieDetailView", params:{"id":id}})
    },
    updateScrollButtonState1() {
      const imageContainer = this.$refs.imageContainer1;
      const scrollLeftEnd = imageContainer.scrollLeft === 0;
      const scrollRightEnd =
        imageContainer.scrollLeft + imageContainer.offsetWidth >=
        imageContainer.scrollWidth;
      this.isScrollLeftEnd1 = scrollLeftEnd;
      this.isScrollRightEnd1 = scrollRightEnd;
      // console.log(this.isScrollLeftEnd1, this.isScrollRightEnd1)
    },
    updateScrollButtonState2() {
      const imageContainer = this.$refs.imageContainer2;
      const scrollLeftEnd = imageContainer.scrollLeft === 0;
      const scrollRightEnd =
        imageContainer.scrollLeft + imageContainer.offsetWidth >=
        imageContainer.scrollWidth;
      this.isScrollLeftEnd2 = scrollLeftEnd;
      this.isScrollRightEnd2 = scrollRightEnd;
      // console.log(this.isScrollLeftEnd1, this.isScrollRightEnd1)
    },
    updateScrollButtonState3() {
      const imageContainer = this.$refs.imageContainer3;
      const scrollLeftEnd = imageContainer.scrollLeft === 0;
      const scrollRightEnd =
        imageContainer.scrollLeft + imageContainer.offsetWidth >=
        imageContainer.scrollWidth;
      this.isScrollLeftEnd3 = scrollLeftEnd;
      this.isScrollRightEnd3 = scrollRightEnd;
      // console.log(this.isScrollLeftEnd1, this.isScrollRightEnd1)
    },
    scrollLeft1() {
      const imageContainer = this.$refs.imageContainer1;
      gsap.to(imageContainer, { scrollLeft: '-=700', duration: 0.5 });
      setTimeout(()=>{
        this.updateScrollButtonState1();
      }, 500)
    },
    scrollRight1() {
      const imageContainer = this.$refs.imageContainer1;
      gsap.to(imageContainer, { scrollLeft: '+=700', duration: 0.5 });
      setTimeout(()=>{
        this.updateScrollButtonState1();
      }, 500)
    },
    scrollLeft2() {
      const imageContainer = this.$refs.imageContainer2;
      gsap.to(imageContainer, { scrollLeft: '-=700', duration: 0.5 });
      setTimeout(()=>{
        this.updateScrollButtonState2();
      }, 500)
    },
    scrollRight2() {
      const imageContainer = this.$refs.imageContainer2;
      gsap.to(imageContainer, { scrollLeft: '+=700', duration: 0.5 });
      setTimeout(()=>{
        this.updateScrollButtonState2();
      }, 500)
    },
    scrollLeft3() {
      const imageContainer = this.$refs.imageContainer3;
      gsap.to(imageContainer, { scrollLeft: '-=700', duration: 0.5 });
      setTimeout(()=>{
        this.updateScrollButtonState3();
      }, 500)
    },
    scrollRight3() {
      const imageContainer = this.$refs.imageContainer3;
      gsap.to(imageContainer, { scrollLeft: '+=700', duration: 0.5 });
      setTimeout(()=>{
        this.updateScrollButtonState3();
      }, 500)
    },
  }
}
// 테스트용
</script>

<style scoped>

div.cont {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  overflow-x: scroll;
  overflow-y:visible;
  padding:20px;
  white-space: nowrap; /* 가로 스크롤을 위해 한 줄에 표시되도록 설정 */
}
img{
  /* display: inline-block; 이미지들이 가로로 나열되도록 설정 */
  margin: 3px;
  width: 210px;
  height: 280px;
  border-radius: 30px;
  object-fit: cover;
}
img:hover {
  transform: scale(1.15);
}

div.cont::-webkit-scrollbar {
    display: none; /* Chrome, Safari, Opera*/
}
h3{
  margin-left:20px;
}
button:disabled {
  opacity: 0.5;
}
button {
  border-radius: 30px;
  background-color: #1f1f1f;
}
.bttn{
  color:rgb(114, 114, 114);
}

@font-face {
  font-family: 'omu_allpretty';
  src: url(@/fonts/omu_allpretty.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}

#h3 {
  font-family: omu_allpretty;
  font-size: 37px
}
</style>