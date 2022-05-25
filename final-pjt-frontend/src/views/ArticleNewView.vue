<template>
  <div class="d-flex justify-content-center mt-5 article-new ">
    <b-card-group deck>
      <b-card
        header="글작성"
        header-tag="header"
      >
      <article-form :article="article" action="create"></article-form>
      </b-card>
    </b-card-group>
  </div>


</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
.article-new {
  font-family: "Do Hyeon", sans-serif;
  font-size: 35px;
}

</style>
