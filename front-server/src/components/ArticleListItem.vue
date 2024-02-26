<template>
  <div>
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}">
    <!-- <h5>{{ article.id }}</h5> -->
    <br>
    <p id="title">글 제목 : {{ article.title }}</p>
    <p id="writer">작성자 : {{ article.username }}</p>
    <br>
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style scoped>
p {
  color: whitesmoke;
  font-family: omu_allpretty;;
  margin-left: 20px;
}

a{
  text-decoration: none;
}

@font-face {
  font-family: 'establish Retrosans';
  src: url(@/fonts/establish_Retrosans.ttf) format('woff');
  font-weight: normal;
  font-style:normal
}

#title {
  font-size: 30px;
}

#writer {
  font-size: 21px;
  text-align: right;
}
</style>
