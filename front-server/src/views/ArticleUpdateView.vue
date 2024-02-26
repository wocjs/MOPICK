<template>
  <div id="ArticleUpdateView">
    <br><br>
    <span id="postUpdate">게시글 수정</span>
    <br>
    <label for="title" class="form-label">글 제목 :&nbsp;&nbsp;&nbsp;</label>
    <input type="text" id="title" class="form-control" v-model="updatedArticleData.title">
    <br><br>
    <label for="content" class="form-label">글 내용 :&nbsp;&nbsp;&nbsp;</label>
    <textarea id="content" cols="30" rows="10" v-model="updatedArticleData.content" class="form-control"></textarea>
    <br><br>
    <div id="updelcont">
    <button class="btn btn-outline-secondary" @click="saveArticle" id="btn">수정</button>&nbsp;&nbsp;&nbsp;
    <button class="btn btn-outline-secondary" @click="cancelUpdate" id="btn">취소</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleUpdateView",
  data() {
    return {
      updatedArticleData: {
        title: '',
        content: ''
      }
    };
  },
  created() {
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
      })
        .then((res) => {
          // console.log(res);
          this.updatedArticleData.title = res.data.title;
          this.updatedArticleData.content = res.data.content;
          this.updatedArticleData.user = res.data.user
        })
        .catch((err) => {
          console.log(err);
        });
    },
    saveArticle() {
      // console.log('saveArticle 실행은 되는중');
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        data: this.updatedArticleData,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log('.then 까지는 들어옴');
          // console.log(res);
          this.$router.push({ name: 'ArticleDetailView', params: { id: this.$route.params.id } })
        })
        .catch((err) => {
          console.log(err);
        });
    },
    cancelUpdate() {
      this.$router.push({ name: 'ArticleDetailView', params: { id: this.$route.params.id } })
    }
  }
};
</script>

<style scoped>
@font-face {
  font-family: 'establish Retrosans';
  src: url(@/fonts/establish_Retrosans.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}

.form-label{
  font-family: omu_allpretty;
  font-size: 25px;
}
.btn btn-outline-secondary{
  float: right;
  font-size: 30px;
  border-radius: 10px;
  border: none;
  color: white;
  font-family: establish Retrosans;
}

#postUpdate{
  font-size: 45px;
  font-family: establish Retrosans;
}

#updelcont {
  text-align: right;
}
</style>