<template>
  <div id="ArticleDetailView">
    <br><br>
    <div v-if="article">
    <h2 id="article_title">{{ article?.title }}</h2> <p><a :v-if="user" @click="toggleArticleLike" class="link" id="articleHeart" :class="{liked: isLiked}">
      {{ isLiked() ? '❤':'❤' }}
    </a> {{ article.likes.length }}  likes</p>
    
    <button :v-if="user" @click="backToList" class="btn btn-outline-secondary" id="goBack">목록으로</button>
    
    </div>
    <br>
    <br>
    <p>작성시간&nbsp;:&nbsp;&nbsp;&nbsp;{{ date1 }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ time1 }}</p>
    <p>수정시간&nbsp;:&nbsp;&nbsp;&nbsp;{{ date2 }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ time2 }}</p>
    <hr><br>
    <p>{{ article?.content }}</p>
    <br><br><br>
    <div id="updelcont">
    <button class="btn btn-outline-secondary" v-if="isAuthorArtice" @click="updateArticleDetail">수정하기</button>
    &nbsp;
    <button class="btn btn-outline-secondary" v-if="isAuthorArtice" @click="deleteArticleDetail">삭제하기</button>
    </div>
    <hr />
    <br>
    <h6>댓글</h6>
    <div class="input-group mb-3">
    <input
      class="form-control"
      id="comment"
      type="text"
      style="margin-right: 10px" 
      aria-label="Create Comment"
      aria-describedby="button-addon2"
      placeholder="댓글 작성시에는 타인을 존중하고, 커뮤니티 가이드를 준수해야 합니다."
      @keyup.enter="createComment"
      v-model="comment"/>
      <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="createComment">등록</button>
    <!-- <button class="link" style="height: 30px" @click="createComment">
      등록
    </button> -->
    </div>
    <br><br><br>
    <p v-for="(log, index) in comments" :key="index" id="commentBox">
    &nbsp; {{ log.username }} : {{ log?.content }}
    <span id="commentLikes">
    <a v-if="user" @click="toggleCommentLike(log)" class="link" id="commentHeart">
      {{ isCommentLiked ? '❤':'❤'}}
    </a>
    <span v-if="log.likes"> {{ log.likes.length }}  likes </span>
    <button class="btn btn-outline-secondary" v-if="isAuthorComment(log)" @click="deleteComment(log)" id="commentDelBtn">❌</button>
    </span>
    </p>
  </div>
</template>

<script>
//###################################################################################
//####################### 헷 갈 림 방 지 용 설 명 ###################################
//################여기 getUserName() 에서 가져온 user는 user의 ID입니다.#############
//###################################################################################
import { mapGetters, mapActions } from 'vuex'
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleDetailView",
  data() {
    return {
      user: null,
      article: null,
      comments: null,
      comment: null,
      date1:'',
      time1:'',
      date2:'',
      time2:'',
      isCommentLiked: null
    };
  },
  created() {
    this.getUserName()
    this.getArticleDetail();
    // this.isArticleLiked()
    // this.toggleArticleLike()
    // console.log(this.user);
  },
  computed: {
    isAuthorArtice() {
      if (this.article && this.user) {
        return this.article.user === this.user
      }
      return false
      },
    ...mapGetters(['getIsLiked']),
    // ...mapGetters(['getIsCommentLiked']),
    // ...mapGetters(['getIsCommentLiked'])

    
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
      })
        .then((res) => {
          console.log(res);
          this.article = res.data;
          let cnt = 0
          this.time1 = ''
          this.date1 = ''
          this.time2 = ''
          this.date2 = ''
          for(let char of this.article.created_at){
            if (char === 'T' || char === ':'){
              cnt += 1
              if (cnt == 2){
                this.time1 += ':'
              }
              continue
            }
            if (cnt === 0){
              this.date1 += char
            }
            else if(cnt <= 2){
              this.time1 += char
            }
          }
          cnt = 0
          for(let char of this.article.updated_at){
            if (char === 'T' || char === ':'){
              cnt += 1
              if (cnt == 2){
                this.time2 += ':'
              }
              continue
            }
            if (cnt === 0){
              this.date2 += char
            }
            else if(cnt <= 2){
              this.time2 += char
            }
          }
          // this.updateCommentLiked(false)
          this.getComment();
          this.getUserName()
          console.log(this.user);
          // this.isLiked = this.toggleArticleLike.isLiked
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateArticleDetail() {
      this.getUserName()
      const updatedArticleData = {
        title: this.article.title,
        content: this.article.content,
        user: this.article.user
      }

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        data: updatedArticleData,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        console.log(res);
        this.article = res.data
        this.$router.push({ name: 'ArticleUpdateView', params: { id: this.$route.params.id } })
      })
      .catch((err) => {
        console.log(err);
      })
    },
    deleteArticleDetail(){
      axios({
        method:'delete',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(() => {
        console.log('삭제되었습니다.')
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err);
      })
    },
    getComment() {
      // console.log('댓글도착');
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
      })
        .then((res) => {
          console.log(res);
          this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    createComment() {
      const user = this.user
      console.log(user);
      const comment = this.comment;
      console.log(comment);
      // console.log('댓글작성');
      axios({
        method: "post",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
        data: { user: user, content: comment },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log('then: 댓글작성');
          this.comment = ''
          this.getComment()
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteComment(comment) {
      console.log(comment.id);
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(() => {
        console.log('댓글 삭제되었습니다.')
        this.getComment()
      })
      .catch((err) => {
        console.log(err);
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
        // console.log('getUserName의 res.data', res.data);   //####잘 가져옴####
      })
      .catch((err) => {
        console.log(err);
      })
    },
    isAuthorComment(log) {
      if ( log.user && this.user) {
      return log.user === this.user
      }
    return false
    },
    ...mapActions(['updateIsLiked']),
    toggleArticleLike() {
      axios({
        method: "post", 
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
          const user = res.data.user
          const isLiked = res.data.is_liked
          const likeCount = res.data.like_count
          console.log('isLiked는', isLiked);
          console.log('res.data는', res.data);
          console.log('likeCount는', likeCount);
          this.updateIsLiked(isLiked, user)
          // this.article.likes = likeCount
          // this.isLiked = !this.isLiked
          this.getArticleDetail()
        ////////////////////////////////////////////////////////
        // this.updateIsLiked(!this.getIsLiked)
          
        // console.log(this.isArticleLiked ? true : false);
      })
      .catch((err) => {
        console.log(err);
      })
      // this.$store.dispatch('changeLike');
    },
    // ...mapActions(['updateCommentLiked']),
    // ...mapActions(['toggleCommentLike']),
    toggleCommentLike(comment) {
      const commentId = comment.id
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        // this.getUserName()
        // const commentId = res.data.comment.id
        const isLiked = res.data.comment_is_liked
        const user = res.data.user
        const likeCount = res.data.comment_like_count
        // console.log('likecount는', likeCount);
        // this.updateCommentLiked({ commentId, isLiked, likeCount, user})
        console.log(user);
        console.log(likeCount);
        this.getArticleDetail()
        console.log('isLiked는', isLiked);
        // this.isLiked = res.data.is_like
        // this.getComment()
        // this.updateCommentLiked({ commentId, isLiked })
      })
      .catch((err) => {
        console.log(err);
      })
    },
    isLiked() {
      return this.$store.isLiked
      // return this.getIsLiked
    },
    // isCommentLiked(commentId) {
    //   return this.getIsCommentLiked(commentId)
    // },
    backToList() {
      this.$router.go(-1)
    },
    // async fetchArticleLikes() {
    //   try {
    //     const res = await axios.get(`${API_URL}/api/v1/articles/${this.$route.params.id}/`)
    //     const articleLikes = res.data
    //     const dtoArticleLikes = articleLikes.map(like => ({
    //       userId: res.data.user.id,
    //       articleId: res.data.likes
    //     }))
    //     console.log(dtoArticleLikes);
    //   } catch (err) {
    //     console.log(err);
    //   }
    // }
  },
  /////////////댓글 좋아요 0525 1240 시도//////////////////
  // toggleCommentLike(comment){
  //   axios({
  //     method: 'post',
  //     url: `${API_URL}/api/v1/comments/${comment.id}/`,
  //     headers: {
  //       Authorization: `Token ${this.$store.state.token}`,
  //     },
  //   })
  //   .then(() => {
  //       this.getComment();
  //     })
  //   .catch((err) => {
  //       console.log(err);
  //     });
  // },
  // isCommentLiked(comment) {
  //   if (this.user && comment.likes.includes(this.user)) {
  //     return true;
  //   }
  //   return false;
  // }
  ////////////////////////////////////////////////////////
};
</script>

<style scoped>
#goBack {
  float: right;
  /* margin-right: 50px; */
}

button {
  border-radius: 5px;
}

a {
  text-decoration: none;
  color: rgb(225, 29, 37);
}

#commentDelBtn {
  float: right;
  border: none;
  /* margin-right: 50px; */
}
  /* #commentLikes {
    float: right;
  } */

#article_title{
  font-family: omu_allpretty;
  color: whitesmoke;
}
@font-face {
  font-family: 'establish Retrosans';
  src: url(@/fonts/establish_Retrosans.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}

#comment{
  background-color:rgb(80, 80, 80);
  /* font-weight: bolder; */
  color: white
}

::placeholder{
  color: #919191;
}

#updelcont {
  text-align: right;
}

#articleHeart {
  cursor: pointer;
}

#commentHeart {
  cursor: pointer;
}

#commentBox {
  justify-content: space-between;
}

#commentLikes {
  float: right;
}

</style>