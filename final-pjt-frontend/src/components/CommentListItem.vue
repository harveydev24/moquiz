<template>
  <ul class="comment-list-item p-0">
    
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="currentUser.username === comment.username && !isEditing">
      <svg @click="deleteComment(payload)" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="red" class="bi bi-file-x-fill cursor" viewBox="0 0 16 16">
        <path d="M12 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM6.854 6.146 8 7.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 8l1.147 1.146a.5.5 0 0 1-.708.708L8 8.707 6.854 9.854a.5.5 0 0 1-.708-.708L7.293 8 6.146 6.854a.5.5 0 1 1 .708-.708z"/>
      </svg>
    </span>

    <router-link :to="{ name: 'profile', params: {username: comment.username} }" >
      {{ comment.username }}
    </router-link>

  </ul>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.id,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['deleteComment']),
    onUpdate() {
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border: 1px solid black;
}
.cursor {cursor: pointer;}
</style>