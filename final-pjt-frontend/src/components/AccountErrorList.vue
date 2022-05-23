<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in authError" :key="field">
      {{ field }}
    </p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "AccountErrorList",
  computed: {
    ...mapGetters(["authError"]),
  },
};
</script>

<style>
.account-error-list {
  color: red;
  font-weight: bolder;
}
</style>
