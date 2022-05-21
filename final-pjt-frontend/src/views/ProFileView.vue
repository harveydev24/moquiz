<template>
  <div class="d-flex justify-content-center mt-5">
    <b-card no-body style="max-width: 20rem">
      <b-card-body>
        <b-card-title class="b-card-title">{{ profile.nickname }}</b-card-title>
        <b-card-sub-title class="mb-2"
          >Follwings: {{ profile.followings_cnt }} Follwers:
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
    ...mapGetters(["profile"]),
  },
  methods: {
    ...mapActions(["fetchProfile"]),
  },

  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style></style>
