<template>
  <span>{{ displayValue }}</span>
</template>

<script>
import gsap from "gsap";

export default {
  name: "AnimatedInteger",
  props: { value: { default: 0 } },

  data() {
    return {
      displayValue: this.value,
      tweenValue: this.value,
    };
  },

  watch: {
    value() {
      gsap.to(this, {
        tweenValue: this.value,
        duration: 1,
        onUpdate: () => {
          this.displayValue = Math.ceil(this.tweenValue);
        },
      });
    },
  },
};
</script>

<style></style>
