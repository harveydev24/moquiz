<template>
  <nav class="navbar">
    <ul>
      <li>
        <router-link :to="{ name: 'home' }">Home</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'ranking' }">Ranking</router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'problem' }">Problem</router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'community' }">Community</router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: {username} }">
          {{ currentUser.username }}'s page
          </router-link>
      </li>
    </ul>
    
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style></style>
