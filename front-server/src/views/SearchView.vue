<template>
  <div>
    <!-- 검색 입력 폼 -->
    <form @submit.prevent="searchMovies()" style="padding:20px">
      <!-- <input class="" type="text" v-model="searchQuery" placeholder="영화 제목을 입력하세요">
      <button type="submit">검색</button> -->
        <div class="input-group mb-3">
          <input v-model="searchQuery" type="text" 
          class="form-control " placeholder="영화, 배우 검색"
          aria-label="Recipient's username" aria-describedby="button-addon2"
          style="background-color:rgb(80, 80, 80); color:#fff">
          <button class="btn btn-outline-secondary" type="submit" id="button-addon2" >검색</button>
        </div>
    </form>
    
    <hr>
    <div v-if="movieResults.length || personResults.length">
      <!-- 검색 결과 -->
      <div v-if="movieResults.length">
        <h2>
            <span id="h3">영화 검색 결과 : {{ movieResults.length }}</span>
          <div style="float:right">
            <button @click="scrollLeft1()" :disabled="isScrollLeftEnd1" id="scrollLeftBtn1" class="bttn">&nbsp;&lt;&nbsp;</button>
            &nbsp;&nbsp;&nbsp;
            <button @click="scrollRight1()" :disabled="isScrollRightEnd1" id="scrollRightBtn1" class="bttn">&nbsp;&gt;&nbsp;</button>
            &nbsp;&nbsp;&nbsp;
          </div>
        </h2>
        <div class="cont" ref="imageContainer1">
          <img v-for="(movie, idx) in movieResults" :key="idx" @click="toDetail(movie.id)" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="이미지를 찾을 수 없음" class="movie-poster">
          <!-- <img v-for="(movie, idx) in movieResults" :key="idx" @click="toDetail(movie.id)" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" :alt="`대체 이미지 - ${movie.title}`" class="movie-poster" onerror="this.src='대체 이미지 경로'"> -->

        </div>
      </div>
        <br>
        <hr>
        <div v-if="personResults.length">
          <h2>
            <span id="h3">인물 검색 결과 : {{ personResults.length }}</span>
            <div style="float:right">
              <button @click="scrollLeft2()" :disabled="isScrollLeftEnd2" id="scrollLeftBtn2" class="bttn">&nbsp;&lt;&nbsp;</button>
              &nbsp;&nbsp;&nbsp;
              <button @click="scrollRight2()" :disabled="isScrollRightEnd2" id="scrollRightBtn2" class="bttn">&nbsp;&gt;&nbsp;</button>
              &nbsp;&nbsp;&nbsp;
            </div>
          </h2>
          <div class="cont" ref="imageContainer2">
            <span v-for="(person, idx) in personResults" :key="idx">
              <img @click="toProfile(person.id)" v-if="person.profile_path" :src="`https://image.tmdb.org/t/p/w500${person.profile_path}`" alt="" class="movie-poster">
            </span>
          </div>

        </div>
      </div>
        <!-- 검색 결과 없음 -->
    </div>
</template>

<script>
import axios from 'axios';
import { gsap } from 'gsap';
export default {
  data() {
    return {
      searchQuery: '',
      movieResults: [],
      personResults: [],
      searchExecuted: false,
      isScrollLeftEnd1: true,
      isScrollRightEnd1: false,
      isScrollLeftEnd2: true,
      isScrollRightEnd2: false,
    }
  },
  methods: {
    // clearSearchQuery() {
    //   this.searchQuery = '';
    //   this.$refs.searchInput.blur();
    // },
    searchMovies() {
      if (this.searchQuery.trim()){
        this.movieResults = []
        this.personResults = []
        const movie_kr_URL = `https://api.themoviedb.org/3/search/movie?api_key=c376bdf28af008508b9156b102e6baf9&language=ko-KR&query=${this.searchQuery}&include_adult=false&language=ko-KR&page=1`;
        const person_en_URL = `https://api.themoviedb.org/3/search/person?api_key=c376bdf28af008508b9156b102e6baf9&language=ko-KR&query=${this.searchQuery}&include_adult=false&language=ko-KR&page=1`;
        axios({
          method:'get',
          url : movie_kr_URL
        })
        .then((res)=>{
          // console.log(res)
          for(let mov of res.data.results){
            if (mov.poster_path){
              this.movieResults.push(mov)
            }
          }
          if(this.movieResults){
            this.searchExecuted = true
          }
          // this.searchQuery = ''
          setTimeout(()=>{
            this.updateScrollButtonState1();
          }, 500)
        })
        axios({
          method:'get',
          url : person_en_URL
        })
        .then((res)=>{
          // console.log(res)
          for(let per of res.data.results){
            if(per.profile_path){
              this.personResults.push(per)
            }
          }
          if(this.personResults){
            this.searchExecuted = true
            // console.log(this.personResults)
          }
          // this.searchQuery = ''
          setTimeout(()=>{
            this.updateScrollButtonState2();
          }, 500)
          
        })
      }
      else{
        alert("검색어를 올바르게 입력해주세요")
        this.searchQuery = ''
      }
      // this.clearSearchQuery();
    },
    toDetail(id){
      // console.log(id)
      this.$router.push({name:"MovieDetailView", params:{"id":id}})
    },
    toProfile(id){
      console.log(id)
      this.$router.push({name:"ProfileView", params:{"id":id}})
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
h2{
  margin-left:20px;
}
button:disabled {
  opacity: 0.5;
}
::placeholder{
  /* font-weight: bolder; */
  color:#919191
}
button {
  border-radius: 10px;
  background-color:rgb(80, 80, 80);
  color: #fff;
  border: solid 1px #ffffff;
}

.bttn{
  color:white;
}

#h3 {
  font-family: omu_allpretty;
}
</style>
