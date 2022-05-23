<template>
  <div>
    <h1>New Article</h1>
    <article-form :article="article" action="create"></article-form>
    <router-link :to="{ name: 'community'}">back</router-link>
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

<style></style>
