<template>
  <div class="articledetail offset card" >
      <div class="card-header">
        <h2 class="card-title cover">
          {{ article.title }}
          <h4>
            <router-link router-link :to="{ name: 'profile', params: {username: article.username} }" style="text-decoration: none; color: info;"> 
              {{ article.username }}
            </router-link>
          </h4>
        </h2>
      </div>

      <div class="card-body">
        <h4 class="card-text">{{ article.content }}
        </h4>
      </div>


      <div v-if="article.like_users.includes(currentUser.pk)">
        <h5 class="m-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="red" class="bi bi-heart-fill" viewBox="0 0 16 16" @click="likeArticle(articlePk)" style="cursor: pointer;">
          <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
        </svg>
          {{likeCount}}
        </h5>
      </div>

      <div v-else>
        <h5 class="m-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="crimson" class="bi bi-heart-fill" viewBox="0 0 16 16" @click="likeArticle(articlePk)" style="cursor: pointer;">
            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
          </svg>
          {{likeCount}}
        </h5>
      </div>

      <b-container>
        <b-row class="h5">
            <b-col>
              <b-table striped hover 
              :items=article.comments
              :fields="fields"


              :select-mode="selectMode"
              ref="selectableTable"
              selectable
              @row-selected="onRowSelected"
              >
                <template #cell(username)="item">
                  <router-link :to="{ name: 'profile', params: {username: item.value} }" style=text-decoration:none;>
                    {{ item.value }}
                  </router-link>
                </template>
              </b-table>
            </b-col>
        </b-row>
      </b-container>

        <ul class="list-group list-group-flush">
          <li class="list-group-item">
            <comment-list :comments="article.comments"></comment-list>
          </li>
        </ul>

        <div class="card-footer cover">
          <router-link :to="{ name: 'community'}" style="text-decoration: none; color: inherit;"  >back</router-link>
          <div v-if="isAuthor">
            <button @click="deleteArticle(articlePk)" class="btn btn-danger">삭제</button>
          </div>
        </div>

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
        
        fields: [
          {key: 'content', label: '댓글'},
          {key: 'username', label: '작성자'},
        ],
        mode: ['single'],
        selectMode: 'single',
        selected: [],
        payload: [],

      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'currentUser']),
      likeCount() {
        return this.article.like_users?.length
      },
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
        'deleteComment',
      ]),

      onRowSelected(item) {
      this.selected = item
      this.payload = {
        articlePk: this.selected[0].article,
        commentPk: this.selected[0].id}
      if (this.currentUser.pk === this.selected[0].user) {
        this.deleteComment(this.payload)
        this.$refs.selectableTable.clearSelected()
      }
      },
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
.articledetail {
  font-size: 25px;
  font-family: "Do Hyeon", sans-serif;
}
.commentlist {
  font-size: 25px;
  font-family: "Do Hyeon", sans-serif;
}
.offset{
  width: 500px;
  margin: 20px auto;  
}
.cover {
  display: flex;
  justify-content: space-between;
}
</style>
