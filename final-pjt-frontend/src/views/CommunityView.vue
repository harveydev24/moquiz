<template>
  <div>
    <h1>Community</h1>
    <ul>
      <li v-for="article in articles" :key="article.pk">
        <!-- 작성자 -->
        {{ article.user }} :
      
        {{ article.title }} 
      
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
