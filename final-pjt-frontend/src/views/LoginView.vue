<template>
  <div class="login-background">
    <b-container class="login-wrapper">
      <b-row class="login-row">
        <b-col class="text-center">
          <b-form @submit.prevent="login(credentials)" class="login-form">
            <h1 class="text-center">로그인</h1>
            <account-error-list v-if="authError"></account-error-list>

            <b-form-input
              id="username"
              v-model="credentials.username"
              type="text"
              placeholder="아이디"
              required
              class="mt-3"
            ></b-form-input>

            <b-form-input
              id="password"
              v-model="credentials.password"
              type="password"
              placeholder="비밀번호"
              required
              class="mt-3"
            ></b-form-input>

            <div class="text-center mt-3">
              <b-button type="submit" block variant="primary">Submit</b-button>
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
  name: "LoginView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["login"]),
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
/* font-family: 'Courgette', cursive;
font-family: 'Do Hyeon', sans-serif;
font-family: 'Oswald', sans-serif; */

.login-background {
  background-image: url("https://assets-global.website-files.com/5e4f771ff45e4c54cb345de3/61401cbff9b93566a1e2d6b0_%2525EB%252589%2525B4%2525EC%25258A%2525A4-%2525EA%2525B7%2525B8%2525EB%2525A6%2525AC%2525EB%252593%25259C-%2525EC%25259D%2525B4%2525EB%2525AF%2525B8%2525EC%2525A7%252580-(2).png");
  background-size: cover;
  overflow: hidden;
  font-family: "Do Hyeon", sans-serif;
}

.login-wrapper {
  width: 100vw;
  height: 100vh;
}

.login-row {
  height: 100%;
}

.login-form {
  position: relative;
  top: 25%;
  margin: auto;
  width: 20%;
  padding: 20px;
  background-color: #ffffff;
  background-color: rgba(255, 255, 255, 0.5);
}
</style>
