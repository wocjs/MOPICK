<template>
  <div v-if="person && movies">
    <br>
    <div id="person-info" class="movie-info">
      <img :src="`https://image.tmdb.org/t/p/w500${person.profile_path}`" :alt="person.name" class="profile-image" />
      <div class="person-description" style="float:left;">
        <br>
        <h1>{{ person.name }}</h1>
        <br>
        <p style="font-size:20px"><b>{{ person.birthday }}</b></p>
        <br>
        <p>{{ person.biography }}</p>
      </div>
    </div>
    <br>
    <hr>
    <p></p>
    <h3> <span id=h3>출연작</span>
      <!-- <div style="float:right">
        <button @click="scrollLeft()" :disabled="isScrollLeftEnd" id="scrollLeftBtn"><span class="bttn">&nbsp;&lt;&nbsp;</span></button>
        &nbsp;&nbsp;&nbsp;
        <button @click="scrollRight()" :disabled="isScrollRightEnd" id="scrollRightBtn"><span class="bttn">&nbsp;&gt;&nbsp;</span></button>
        &nbsp;&nbsp;&nbsp;
      </div> -->
    </h3>
    <div class="cont" ref="imageContainer">
      <img class="relimg" @click="toDetail(movie.id)" v-for="(movie, index) in movies" :key="index" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
    </div>
  </div>
</template>


<script>
import axios from 'axios';
const API_KEY = 'c376bdf28af008508b9156b102e6baf9'
export default {
  data() {
    return {
      person: null,
      // isScrollLeftEnd:true,
      // isScrollRightEnd:false,
      movies: [],
    }
  },
  created() {
    this.getPersonDetail()
    this.getCredits()
  },
  computed: {
    personID() {
      return this.$route.params.id
    },
  },
  methods: {
    getPersonDetail() {
      const profileDetailURL = `https://api.themoviedb.org/3/person/${this.personID}?language=ko-KR`
      const profileDetailURL_US = `https://api.themoviedb.org/3/person/${this.personID}?language=en-US`
      axios.get(profileDetailURL, {
        params: {
          api_key: API_KEY
        }
      })
      .then((res) => {
        console.log(res)
        this.person = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
      axios.get(profileDetailURL_US, {
        params: {
          api_key: API_KEY
        }
      })
      .then((res) => {
        console.log(res)
        if (this.person.biography.length === 0){
          this.person.biography = res.data.biography
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getCredits(){
      
      const creditURL = `https://api.themoviedb.org/3/person/${this.personID}/movie_credits?language=ko-KR`
      axios.get(creditURL, {
        params:{
          api_key:API_KEY
        }
      })
      .then((res)=>{
        // console.log(res.data.cast)
        // this.movies = res.data.cast
        for (let movie of res.data.cast){
          if (movie.poster_path){
            this.movies.push(movie)
          }
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    toDetail(id){
      this.$router.push({
        name:"MovieDetailView",
        params:{"id":id}
      })
    }
  }
}
</script>
<style scoped>
  .profile-image {
    width: 210px;
    height: 300px;
    border-radius: 30px;
    margin-right: 20px;
    margin-top: 30px;
  }
  #person-info{
    display: flex;
    justify-content: left;
    margin-top: 20px;
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

#h3 {
  font-family: omu_allpretty;
}
</style>
