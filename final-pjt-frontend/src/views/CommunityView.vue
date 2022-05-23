<template>
  <div>
    <h1>Community</h1>
    <h3>
      <router-link :to="{name: 'articleNew'}">new article</router-link>
    </h3>
    <ul>
      
      <li v-for="article in articles" :key="article.id">
        
        {{ article.username }} :
        
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.id} }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
   
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'CommunityView',
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style></style>
