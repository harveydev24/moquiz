<template>
  <div class="community">
    <b-container>
      <b-row>
        <b-col>
          <b-table striped hover 
          :items=lists 
          :fields="fields"
          :select-mode="selectMode"
          ref="selectableTable"
          selectable
          @row-selected="onRowSelected"
          >
          </b-table>

        </b-col>
      </b-row>
      
      <div align=right >
        <router-link :to="{name: 'articleNew'}" style="text-decoration: none; color: inherit;">글작성</router-link>
      </div>


      <div class="mt-3">
        <b-pagination 
        v-model="currentPage" 
        :total-rows="totalRows" align="center"
        :per-page="perPage"/>
      </div>

    </b-container>
  </div>

</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    name: 'CommunityView',
    
    data(){
      return {
        currentPage: 1,
        perPage: 7,
        mode: ['single'],
        fields: [
          {key: 'id', label: '글번호'},
          {key: 'title', label: '글제목'},
          {key: 'username', label: '작성자'},
        ],
        selectMode: 'single',
        selected: []
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
      onRowSelected(item) {
      this.selected = item
      this.$router.push({ name: 'article', params: {articlePk: this.selected[0].id} })
      },

    },
    created() {
      this.fetchArticles()
      },
    }
</script>



<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
.community {
  font-size: 25px;
  font-family: "Do Hyeon", sans-serif;
}
.myList {
  padding: 20px;
}


</style>
