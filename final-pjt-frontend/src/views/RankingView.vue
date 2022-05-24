<template>
  <div class="ranking">
    <b-container>
      <b-row
        ><b-col> <b-table striped hover :items="users"></b-table> </b-col
      ></b-row>
    </b-container>
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
        let rank = 1
        res.data.forEach((user) => {
          let myUser = {}
          myUser.rank = rank
          myUser.nickname = user.nickname
          myUser.score = user.score
          myUser.correct = user.correct
          myUser.wrong = user.wrong
          this.users.push(myUser)
          rank += 1
        })
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
/* font-family: 'Courgette', cursive;
font-family: 'Do Hyeon', sans-serif;
font-family: 'Oswald', sans-serif; */
.ranking {
  font-size: 25px;
  font-family: "Do Hyeon", sans-serif;
}
</style>
