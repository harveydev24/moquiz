<template>
  <div class="d-flex justify-content-center mt-5 b-card">
    <b-card no-body style="width: 25rem">
      <b-card-body>
        <div v-if="isMe">
          <div v-if="isFollow">
            <button @click="followUser(profile.id)" class="btn btn-outline-danger" style="float:right">언팔로우</button>
          </div>

          <div v-else>
            <button @click="followUser(profile.id)" class="btn btn-outline-primary" style="float:right">팔로우</button>
          </div>
        </div>
        <b-card-title class="b-card-title">{{ profile.nickname }}</b-card-title>
          



        <b-card-sub-title class="mb-2 b-card-subtitle">
          Follwings: {{ profile.followings_cnt }} Follwers:
          {{ profile.followers_cnt }}
          
        </b-card-sub-title>
      </b-card-body>

      <b-list-group flush>
        <b-list-group-item
          >획득한 점수:
          <animated-integer :value="profile.score"></animated-integer
        ></b-list-group-item>
        <b-list-group-item
          >맞힌 문제:
          <animated-integer :value="profile.correct"></animated-integer
        ></b-list-group-item>
        <b-list-group-item
          >틀린 문제:
          <animated-integer :value="profile.wrong"></animated-integer
        ></b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import AnimatedInteger from "../components/AnimatedInteger.vue";

export default {
  name: "ProFileView",
  components: { AnimatedInteger },

  computed: {
    ...mapGetters(["profile", "isFollow", "isMe"]),
  },
  methods: {
    ...mapActions(["fetchProfile", "followUser"]),
  },

  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
/* font-family: 'Courgette', cursive;
font-family: 'Do Hyeon', sans-serif;
font-family: 'Oswald', sans-serif; */
.b-card-title {
  font-family: "Do Hyeon", sans-serif;
  font-size: 60px;
}
.b-card-subtitle {
  font-family: "Do Hyeon", sans-serif;
  font-size: 30px;
}

.b-card {
  font-family: "Do Hyeon", sans-serif;
  font-size: 50px;
}
</style>
