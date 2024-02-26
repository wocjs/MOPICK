<template>
  <div id="ArticleDetailView">
    <!-- ... existing code ... -->
    <br><br>
    <button class="link" @click="likeArticle">좋아요</button>  <!-- Added like button -->
    <p>좋아요 수: {{ article?.likes }}</p>  <!-- Display the number of likes -->
    <hr />
    <!-- ... existing code ... -->
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
// ... existing code ...

export default {
  // ... existing code ...
  methods: {
    // ... existing methods ...
    likeArticle() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log('게시물 좋아요');
          this.getArticleDetail(); // Refresh the article data after liking
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // ... existing methods ...
  },
};
</script>
