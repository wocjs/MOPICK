<template>
  <div class="article-list">
    <!-- <h3 id="post_list">&nbsp;&nbsp;&nbsp;글 목록</h3> -->
    <!-- <hr> -->
    <ArticleListItem 
    v-for="article in articles" :key="article.id" :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style scoped>
.article-list {
  text-align: start;
  color: whitesmoke;
}

#post_list {
  font-family: omu_allpretty;;
  color: whitesmoke;
}
@font-face {
  font-family: 'establish Retrosans';
  src: url(@/fonts/establish_Retrosans.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}
</style>
