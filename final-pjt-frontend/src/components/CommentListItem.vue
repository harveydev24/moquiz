<template>
  <li class="comment-list-item">
    <router-link :to="{ name: 'profile', params: {username: comment.username} }" >
      {{ comment.username }}
    </router-link>
    
    <span v-if="!isEditing">{{ payload.content }}</span>
    
    <span v-if="currentUser.username === comment.username && !isEditing">
      <button @click="deleteComment(payload)">Delete</button>
    </span>
  </li>
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
  border: 1px solid green;

}
</style>