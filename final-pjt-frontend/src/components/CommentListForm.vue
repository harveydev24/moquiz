<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <h4>
      <label for="comment">댓글: </label>
    </h4>
    <textarea name="" id="comment" cols="40" rows="2" v-model="content" required></textarea><br>
    <div align="right">
      <button  class="btn btn-secondary">댓글달기</button>
    </div>
  </form>
</template>


<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>