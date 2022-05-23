<template>
  <div>
    <h1>{{ article.title }}</h1>
    
    <p>
      {{ article.content }}
    </p>
    <div v-if="isAuthor">
      <button @click="deleteArticle(articlePk)">Delete</button>
    </div>

    <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{likeCount}}</button>
    </div>

    <router-link :to="{ name: 'community'}">back</router-link>
    
    <hr />
    <comment-list :comments="article.comments"></comment-list>
    
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'ArticleDetail',
    components: { CommentList },  
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style></style>
