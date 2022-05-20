<template>
  <div>
    <p>{{ profile.username }}</p>
    <p>3</p>
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
    console.log(payload)
    this.fetchProfile(payload)
    
  },
}
</script>
