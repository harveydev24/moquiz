<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="/" class="ms-3 brand"
        >Moquiz on the SSAFY</b-navbar-brand
      >

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item>
            <router-link class="link" :to="{ name: 'home' }">홈</router-link>
          </b-nav-item>
          <b-nav-item v-if="!isLoggedIn"
            ><router-link class="link" :to="{ name: 'login' }"
              >로그인</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="!isLoggedIn"
            ><router-link class="link" :to="{ name: 'signup' }"
              >회원가입</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link class="link" :to="{ name: 'community' }"
              >커뮤니티</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link class="link" :to="{ name: 'ranking' }"
              >랭킹</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link class="link" :to="{ name: 'problem' }"
              >퀴즈</router-link
            ></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <router-link
              class="link"
              @click.native="onClick"
              :to="{ name: 'profile', params: { username } }"
            >
              마이페이지
            </router-link></b-nav-item
          >
          <b-nav-item v-if="isLoggedIn">
            <span class="link" @click="logout"> 로그아웃 </span></b-nav-item
          >
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "NavBar",
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser", "profile"]),
    username() {
      return this.currentUser.username ? this.currentUser.username : "guest";
    },
  },
  methods: {
    ...mapActions(["logout", "fetchProfile"]),
    onClick() {
      const payload = { username: this.username };
      this.fetchProfile(payload);
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
/* font-family: 'Courgette', cursive;
font-family: 'Do Hyeon', sans-serif;
font-family: 'Oswald', sans-serif; */
.brand {
  font-family: "Courgette", cursive;
}

.link {
  text-decoration: none;
  color: white;
  font-family: "Do Hyeon", sans-serif;
  font-size: 25px;
}

.link:hover {
  color: rgb(116, 116, 116);
}
</style>
