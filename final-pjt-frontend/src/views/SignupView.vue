<template>
  <div class="signup-background">
    <b-container class="signup-wrapper">
      <b-row class="signup-row">
        <b-col class="text-center">
          <h1 class="banner"><b>Moquiz on the SSAFY</b></h1>
          <b-form @submit.prevent="signup(credentials)" class="signup-form">
            <h1 class="text-center">회원가입</h1>
            <account-error-list v-if="authError"></account-error-list>

            <b-form-input
              id="username"
              v-model="credentials.username"
              type="text"
              placeholder="아이디"
              required
              autofocus
              class="mt-3"
            ></b-form-input>
            <b-form-input
              id="nickname"
              v-model="credentials.nickname"
              type="text"
              placeholder="별명"
              required
              class="mt-3"
            ></b-form-input>
            <b-form-input
              id="password1"
              v-model="credentials.password1"
              type="password"
              placeholder="비밀번호"
              required
              class="mt-3"
            ></b-form-input>
            <b-form-input
              id="password2"
              v-model="credentials.password2"
              type="password"
              placeholder="비밀번호 확인"
              required
              class="mt-3"
            ></b-form-input>
            <div class="text-center mt-3">
              <b-button type="submit" block variant="primary"
                >가입하기</b-button
              >
            </div>
          </b-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "SignupView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password1: "",
        password2: "",
        nickname: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["signup"]),
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
/* font-family: 'Courgette', cursive;
font-family: 'Do Hyeon', sans-serif;
font-family: 'Oswald', sans-serif; */

.banner {
  text-align: center;
  font-size: 7rem;
  font-family: "Courgette", cursive;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  user-select: none;
  margin-top: 3%;
}

.banner b {
  color: #fee;
  text-shadow: 0 -40px 140px, 0 0 2px, 0 0 0.3em #ff4444, 0 0 0.3em #ff4444,
    0 0 0.1em #ff4444, 0 10px 3px #000;
}

.signup-background {
  background-image: url("../assets/background_image.png");
  background-size: cover;
  overflow: hidden;
  font-family: "Do Hyeon", sans-serif;
}

.signup-wrapper {
  width: 100vw;
  height: 100vh;
}

.signup-row {
  height: 100%;
}

.signup-form {
  position: relative;
  top: 5%;
  margin: auto;
  width: 20%;
  padding: 20px;
  background-color: #ffffff;
  background-color: rgba(255, 255, 255, 0.5);
}
</style>
