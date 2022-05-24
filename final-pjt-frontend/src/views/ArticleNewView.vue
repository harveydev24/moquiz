<template>
  <div class="d-flex justify-content-center mt-5 b-card">
    <b-card no-body style="width: 40rem">
      <b-card-body>
        <b-card-title class="b-card-title">New Article</b-card-title>
      </b-card-body>

      <b-list-group flush>
        <b-list-group-item>
          <article-form :article="article" action="create"></article-form>
          <router-link :to="{ name: 'community'}">back</router-link>
        </b-list-group-item>
      </b-list-group>
    </b-card>
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
.b-card-title {
  font-family: "Do Hyeon", sans-serif;
  font-size: 60px;
}
.b-card-subtitle {
  font-family: "Do Hyeon", sans-serif;
  font-size: 30px;
}

.b-card {
  font-family: "Do Hyeon", sans-serif;
  font-size: 50px;
}
</style>
