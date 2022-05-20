<template>
  <div class="ranking">
    <b-table striped hover :items="users"></b-table>
  </div>
</template>

<script>
import axios from "axios";
import drf from "@/api/drf";

export default {
  name: "RankingView",
  components: {},
  computed: {},
  data() {
    return {
      users: [],
    };
  },
  created() {
    axios({
      url: drf.accounts.ranking(),
      method: "get",
      headers: this.$store.getters.authHeader,
    })
      .then((res) => {
        this.users = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
