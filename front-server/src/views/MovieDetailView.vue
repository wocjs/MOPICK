<template>
  <div class="movie-details" v-if="movie">
    <div v-if="videoURL" class="video-container">
      <div class="video-wrapper">
        <iframe :src="videoURL" frameborder="0" class="video-frame"></iframe>
      </div>
    </div>
    <hr>
    <div class="movie-info"
    :style="{ backgroundImage: `linear-gradient( rgba(0, 0, 0, 0.75), 
    rgba(0, 0, 0, 0.75) ),
     url(https://image.tmdb.org/t/p/original${movie.backdrop_path})`,
     
     }" style="min-height:480px;padding:20px">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" id="movie-poster">
      <div class="movie-description" style="float:left;">
        <br>
        <h1>{{ movie.title }}</h1>
        <p>{{ movie.release_date }}</p>
        <br>
        <p style="min-height:670">{{ movie.overview }}</p>
        <ul>
          <br>
          <b>장르 : </b>
          <li v-for="genre in movie.genres" :key="genre.id">{{ genre.name }}</li>
        </ul>
      </div>
    </div>
    <hr>
    <div v-if="credits">
      <h3><span id=h3>
        출연진</span>
        <div style="float:right">
          <button @click="scrollLeft2()" :disabled="isScrollLeftEnd2" id="scrollLeftBtn2"><span class="bttn">&nbsp;&lt;&nbsp;</span></button>
          &nbsp;&nbsp;&nbsp;
          <button @click="scrollRight2()" :disabled="isScrollRightEnd2" id="scrollRightBtn2"><span class="bttn">&nbsp;&gt;&nbsp;</span></button>
          &nbsp;&nbsp;&nbsp;
        </div>
      </h3>
      <div class="cont" ref="imageContainer2">
        <img class="relimg" @click="toProfile(person.id)" v-for="(person, index) in credits" :key="index" :src="`https://image.tmdb.org/t/p/w500${person.profile_path}`" alt="">
      </div>
    </div>
    <div v-if="simMovies.length">
      <hr>
      <h3><span id=h3>
        {{ movie.title }}과 비슷한 영화</span>
        <div style="float:right">
          <button @click="scrollLeft1()" :disabled="isScrollLeftEnd1" id="scrollLeftBtn1"><span class="bttn">&nbsp;&lt;&nbsp;</span></button>
          &nbsp;&nbsp;&nbsp;
          <button @click="scrollRight1()" :disabled="isScrollRightEnd1" id="scrollRightBtn1"><span class="bttn">&nbsp;&gt;&nbsp;</span></button>
          &nbsp;&nbsp;&nbsp;
        </div>
      </h3>
      <div class="cont" ref="imageContainer1">
        <img class="relimg" @click="toDetail(movie.id)" v-for="(movie, index) in simMovies" :key="index" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
      </div>
      <br><br>
    </div>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import axios from 'axios'
import { gsap } from 'gsap';
const API_KEY = 'c376bdf28af008508b9156b102e6baf9'
/*
id를 
*/
export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: null,
      videoURL : null,
      videoQuery : null,
      youtubeKey:null,
      simMovies:[],
      movie_id : this.$route.params.id,
      isScrollLeftEnd1:true,
      isScrollRightEnd1:false,
      isScrollLeftEnd2:true,
      isScrollRightEnd2:false,
      credits:[]
    }
  },
  watch:{
    movie_id(){
      // console.log('movie_id', this.movie_id)
      this.getMovieDetails()
      this.simMovies=[]
      this.getSimMovies()
      this.credits=[]
      this.getCredits()
    }
  },
  computed: {
    movieID() {
      return this.$route.params.id
    },
    API_URL() {
      return `https://api.themoviedb.org/3/movie/${this.movieID}?language=ko-KR`
    },
  },
  created() {
    this.getMovieDetails(),
    this.getSimMovies(),
    this.getCredits()
  },
  beforeRouteUpdate(to, from, next){
    // console.log(to, from)
    // console.log('to.params.id', to.params.id)
    this.movie_id = to.params.id
    next()
  },
  methods: {
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
    getMovieDetails() {
      // console.log('########################')
      // console.log(this.MOVIEID)
      axios.get(this.API_URL, {
          params: {
            api_key: API_KEY
          }
        })
        .then(response => {
          console.log(response)
          this.movie = response.data
          this.videoQuery = this.movie.title
          console.log(`https://image.tmdb.org/t/p/original${this.movie.backdrop_path}`)
          this.getVideo()
        })
        .catch(error => {
          console.log(error)
        })
    },
    toDetail(id){
      this.$router.push({
        name:"MovieDetailView",
        params:{"id":id}
      })
    },
    getVideo(){
      // const api_key = process.env.VUE_APP_YOUTUBE_API_KEY
      // const searchURL = `https://www.googleapis.com/youtube/v3/search?key=${api_key}&part=snippet&type=video&q=${this.videoQuery}%20예고편`
      // axios({
      //   method:'get',
      //   url: searchURL
      // })
      // .then((res)=>{
      //   this.videoURL = `https://www.youtube.com/embed/${res.data.items[0].id.videoId}`
      //   this.videoName = res.data.items[0].snippet.title
      //   console.log(res.data.items[0].snippet.title)
      // })
      // .catch((err)=>{
      //   console.log(err)
      // })
      const tmdbVideoURL = `https://api.themoviedb.org/3/movie/${this.movieID}/videos?api_key=${API_KEY}&language=en-US`
      axios({
        method:'get',
        url:tmdbVideoURL
      })
      .then((res)=>{
        // console.log(res.data)
        // const youtubeKey = res.data.results[5].key
        for(let data of res.data.results){
          if (data.type.includes("Trailer")){
            this.youtubeKey = data.key
            break
          }
        }
        if (this.youtubeKey == null){
          this.youtubeKey = res.data.result[0].key
        }
        // console.log('##########')
        // console.log(this.youtubeKey)
        this.videoURL = `https://www.youtube.com/embed/${this.youtubeKey}`
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    toProfile(id){
      console.log(id)
      this.$router.push({name:"ProfileView", params:{"id":id}})
    },
    updateScrollButtonState1() {
      const imageContainer = this.$refs.imageContainer1;
      if (imageContainer) {
        const scrollLeftEnd = imageContainer.scrollLeft === 0;
        const scrollRightEnd =
          imageContainer.scrollLeft + imageContainer.offsetWidth >=
          imageContainer.scrollWidth;
        this.isScrollLeftEnd1 = scrollLeftEnd;
        this.isScrollRightEnd1 = scrollRightEnd;
        // console.log(this.isScrollLeftEnd1, this.isScrollRightEnd1)
      }
    },
    updateScrollButtonState2() {
      const imageContainer = this.$refs.imageContainer2;
      if (imageContainer) {
        const scrollLeftEnd = imageContainer.scrollLeft === 0;
        const scrollRightEnd =
          imageContainer.scrollLeft + imageContainer.offsetWidth >=
          imageContainer.scrollWidth;
        this.isScrollLeftEnd2 = scrollLeftEnd;
        this.isScrollRightEnd2 = scrollRightEnd;
        // console.log(this.isScrollLeftEnd1, this.isScrollRightEnd1)
      }
    },
    getSimMovies(){
      // console.log(this.movieID)
      // const token = this.$store.state.token;
      const URL = `https://api.themoviedb.org/3/movie/${this.movieID}/similar?api_key=${API_KEY}&language=ko-KR&page=1&certification_country=KR&certification.lte=15`
      axios({
        method:'get',
        url:URL
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
        setTimeout(()=>{
          this.updateScrollButtonState1();
        }, 500)
      })
      .catch((errr)=>{
        console.log(errr)
      })
    },
    
    // toDetail(id){
    //   console.log(id)
      
    // },
    getCredits(){
      const creditsURL = `https://api.themoviedb.org/3/movie/${this.movie_id}/credits?language=ko-KR`
      axios.get(creditsURL,{
        params:{
          api_key:API_KEY
        }
      })
      .then((res)=>{
        const cast = res.data.cast
        for (let ps of cast){
          if (ps.profile_path){
            this.credits.push(ps)
          }
        }
      })
      .catch((err)=>{
        console.log(err)
      })
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
  }
}
</script>

<style scoped>
.movie-details {
  padding: 20px;
}

/* .movie-details img {
  max-width: 300px;
  margin-bottom: 10px;
} */

.movie-details h1 {
  font-size: 26px;
  font-weight: bold;
  margin-bottom: 10px;
}

.movie-details p {
  margin-bottom: 5px;
  color: #ffffff;
}

.movie-details ul {
  margin-top: 10px;
  list-style-type: none;
  padding: 0;
}

.movie-details ul li {
  display: inline-block;
  margin-right: 10px;
}

.video-container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.video-wrapper {
  position: relative;
  width: 100%;
  padding-bottom: min(450px, calc(100% / (16 / 9)));
  max-width: 800px;
  max-height: 450px;
  margin: 0 auto;
}

.video-frame {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  
  max-width: 800px;
  max-height:450px;
}

.video-backdrop {
  position: center;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
  background-size: 'cover';
}

.movie-info {
  display: flex;
  /* justify-content: center; */
  background-size: cover;
  background-position: center;
  object-fit: contain;
  align-content: center;
}

.movie-description {
  margin-left: 20px;
}

.recommendation {
  margin-top: 20px;
  margin-left: 20px;
}
div.cont {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  overflow-x: scroll;
  overflow-y:visible;
  padding:20px;
  white-space: nowrap; /* 가로 스크롤을 위해 한 줄에 표시되도록 설정 */
}
.relimg{
  /* display: inline-block; 이미지들이 가로로 나열되도록 설정 */
  margin: 3px;
  width: 159px;
  height: 212px;
  border-radius: 20px;
  object-fit: cover;
}
.relimg:hover {
  transform: scale(1.15);
}

#movie-poster {
  width: 300px;
  height: 400px;
  border-radius: 10px;
  margin-top: auto;
  margin-bottom:auto;
  float:left
}


div.cont::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera*/
}
button {
  border-radius: 300px;
  background-color: #666666;
}
button:disabled {
  opacity: 0.5;
}
.bttn{
  color:white;
}

#h3 {
  font-family: omu_allpretty;
}
</style>