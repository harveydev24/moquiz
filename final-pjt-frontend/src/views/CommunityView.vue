<template>
  <div id="app" class="col-sm-12">
    
    <div class="offset">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>글 번호</th>
          <th>글 제목</th>
          <th>작성자</th>
        </tr>
      </thead>
      <tbody>
      <tr v-for="article in lists" :key="article.id">
        <p>{{article.id}}</p>
        
        <td>
          <router-link 
            :to="{ name: 'article', params: {articlePk: article.id} }">
            {{ article.title }}
          </router-link>
        </td>
        <td>
          <router-link :to="{ name: 'profile', params: {username: article.username} }"> 
          {{ article.username }}</router-link>
        </td>
      </tr>
      </tbody>
    </table>
    <router-link :to="{name: 'articleNew'}">글작성</router-link>
    <b-pagination
     :total-rows="totalRows" 
     v-model="currentPage"
     :per-page="perPage"/>

    </div>
    
  </div>


  <!-- <div>
    <h1>Community</h1>
    <h3>
      <router-link :to="{name: 'articleNew'}">new article</router-link>
      
    </h3>
    <ul>
      <li v-for="article in articles" :key="article.id">
        <router-link
          :to="{ name: 'profile', params: {username: article.username} }"> 
          {{ article.username }}</router-link> : 
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.id} }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
  </div> -->
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'CommunityView',
    data(){
      return {
        currentPage: 1,
        perPage: 7,
      };
    },
    computed: {
      ...mapGetters(['articles']),

      lists () {
      const items = this.articles;
      return items.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage
      )
      },
      totalRows () {
      return this.articles.length
      }

    },
    methods: {
      ...mapActions(['fetchArticles']),
    },
    created() {
      this.fetchArticles()
      },
    }
</script>

<style>
.offset{
  width: 500px !important;
  margin: 20px auto;  
}
.myList {
  padding: 20px;
}
</style>
