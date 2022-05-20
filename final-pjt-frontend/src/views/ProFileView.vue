<template>
  <div class="d-flex justify-content-center mt-5">
    <b-card no-body style="max-width: 20rem">
      <b-card-body>
        <b-card-title>{{ profile.nickname }}</b-card-title>
        <b-card-sub-title class="mb-2"
          >Follwings: {{ profile.followings_cnt }} Follwers:
          {{ profile.followers_cnt }}
        </b-card-sub-title>
      </b-card-body>

      <b-list-group flush>
        <b-list-group-item>획득한 점수: {{ profile.score }}</b-list-group-item>
        <b-list-group-item>맞힌 문제: {{ profile.correct }}</b-list-group-item>
        <b-list-group-item>틀린 문제: {{ profile.wrong }}</b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProFileView",
  computed: {
    ...mapGetters(["profile"]),
  },
  methods: {
    ...mapActions(["fetchProfile"]),
  },

  created() {
    const payload = { username: this.$route.params.username };
    console.log(payload);
    this.fetchProfile(payload);
  },
};
</script>
