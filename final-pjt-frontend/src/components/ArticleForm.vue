<template>
  <div class="article_cover">
    <form @submit.prevent="onSubmit">
      <div>
        <label for="title" class="article-form-title">제목: </label>
        <textarea id="title" cols="30" rows="1" v-model="newArticle.title" required></textarea>
      </div>
      <div>
        <label for="content" class="article-form-content">내용: </label>
        <textarea id="content" cols="30" rows="3" v-model="newArticle.content" required></textarea>
      </div>
      <div class="article-form-cover">
        <router-link :to="{ name: 'community'}" style="text-decoration: none; color:black">back</router-link>
        <button class="btn-lg btn-secondary">작성</button>
        
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style>
.article_cover {
  display: flex;
  justify-content: space-between;
  font-size: 30px;
}
.article-form-title {
  display: flex;
  justify-content: space-between;
  font-size: 30px;
}
.article-form-content {
  display: flex;
  justify-content: space-between;
  font-size: 25px;
}
.article-form-cover{
  display: flex;
  justify-content: space-between;
}
</style>
