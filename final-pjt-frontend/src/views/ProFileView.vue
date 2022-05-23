<template>
  <div>
    <p>{{ profile.nickname }}</p>
    <p>{{ profile }}</p>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProFileView',
  computed: {
    ...mapGetters(['profile']),
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
