<template>
  <div class="create_cont">
    <br><br>
    <span id='postCreate'>게시글 작성</span>
    <br>
    <div class="mb-3">
    <form @submit.prevent="createArticle">
      <label for="title" class="form-label">글 제목 :&nbsp;&nbsp;&nbsp;</label>
      <input type="text" id="title" class="form-control" v-model.trim="title"><br><br>
      <label for="content" class="form-label">글 내용 :&nbsp;&nbsp;&nbsp;</label>
      <textarea id="content" cols="30" rows="10" v-model="content" class="form-control"></textarea><br>
      
    <input type="submit" id="submit" value="작성" class="btn btn-outline-secondary">
    </form>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      user: null,
      // username: null,
      title: null,
      content: null,
    }
  },
  created() {
    this.getUserName()
  },
  methods: {
    createArticle() {
      // this.getUserName()
      const user = this.user
      // console.log(user)
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content){
        alert('내용을 입력해주세요')
        return
      }
      // console.log(title)
      // console.log(content)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: { user, title, content },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'ArticleView'})
        // console.log(user)              
        // console.log(title)
        // console.log(content)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUserName() {
      axios({
        method:'get',
        url: `${API_URL}/api/v1/articles/current_user/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.user = res.data.user
        // console.log('getUserName의',this.user);   ####잘 가져옴####
      })
      .catch((err) => {
        console.log(err);
      })
    }
  }
}
</script>

<style scoped>
@font-face {
  font-family: 'establish Retrosans';
  src: url(@/fonts/establish_Retrosans.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}

/* .create_cont{
  font-family: establish Retrosans;
} */

#submit{
  float: right;
  font-size: 30px;
  border-radius: 10px;
  border: none;
  color: white;
  font-family: omu_allpretty;
}

#postCreate{
  font-size: 45px;
  font-family: omu_allpretty;
}

.form-label{
  font-family: omu_allpretty;
  font-size: 25px;
}
</style>
