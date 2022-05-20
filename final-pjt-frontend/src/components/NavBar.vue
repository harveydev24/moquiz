<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">Moquiz on the SSAFY</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item>
            <router-link class="link" :to="{ name: 'home' }">Home</router-link>
          </b-nav-item>
          <b-nav-item v-if="!isLoggedIn"
            ><router-link class="link" :to="{ name: 'login' }"
              >Login</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="!isLoggedIn"
            ><router-link class="link" :to="{ name: 'signup' }"
              >Signup</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link class="link" :to="{ name: 'community' }"
              >Community</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link class="link" :to="{ name: 'ranking' }"
              >Ranking</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link class="link" :to="{ name: 'problem' }"
              >Quiz</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link
              class="link"
              :to="{ name: 'profile', params: { username } }"
            >
              {{ currentUser.username }}'s page
            </router-link></b-nav-item
          >
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "NavBar",
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
    username() {
      return this.currentUser.username ? this.currentUser.username : "guest";
    },
  },
};
</script>

<style>
.link {
  text-decoration: none;
  color: white;
}
</style>
