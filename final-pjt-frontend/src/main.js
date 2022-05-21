import Vue from "vue";

import App from "./App.vue";
import store from "./store";
import router from "./router";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import gsap from "gsap";
import Notification from "vue-notification";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(gsap);
Vue.use(Notification);

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");
