import router from "@/router";
import axios from "axios";
import drf from "@/api/drf";

export default {
  state: {
    token: localStorage.getItem("token") || "",
    currentUser: {},
    profile: {},
    authError: null,
  },

  getters: {
    isLoggedIn: (state) => !!state.token,
    
    isFollow: (state,getters) => {
      let check = false
      getters.profile.followers.forEach(function(element){
        if(element.id === state.currentUser.pk)check=true
      })
      return check


    //   let check = false
    //   getters.profile.foreach(followers => {
    //     if(followers.id === state.currentUser.pk)check=true
    //   })
    //   return check
      
    //   arr.forEach(function(element){
    //     console.log(element); // 0 1 2 3 4 5 6 7 8 9 10
    // });
      // return getters.profile.followers.includes(state.currentUser.pk)
      // return getters.profile
      
      // return getters.profile
      // return state.currentUser.pk
      // return state.currentUser.pk  
    },


    isMe: (state) => {
      return state.currentUser.username !== state.profile.nickname
    },



    currentUser: (state) => state.currentUser,
    profile: (state) => state.profile,
    authError: (state) => state.authError,
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),
  },

  mutations: {
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, profile) => (state.profile = profile),
    SET_AUTH_ERROR: (state, error) => (state.authError = error),
  },

  actions: {
    saveToken({ commit }, token) {
      commit("SET_TOKEN", token);
      localStorage.setItem("token", token);
    },

    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.setItem("token", "");
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          router.push({ name: "home" });
        })
        .catch((err) => {
          console.error(err.response.data);
          commit("SET_AUTH_ERROR", err.response.data);
        });
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          router.push({ name: "home" });
        })
        .catch((err) => {
          console.error(err.response.data);
          commit("SET_AUTH_ERROR", err.response.data);
        });
    },

    logout({ getters, dispatch }) {
      console.log("first");
      axios({
        url: drf.accounts.logout(),
        method: "post",

        headers: getters.authHeader,
      })
        .then(() => {
          dispatch("removeToken");
          alert("성공적으로 logout!");
          router.push({ name: "login" });
        })
        .error((err) => {
          console.error(err.response);
        });
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: "get",
          headers: getters.authHeader,
        })
          .then((res) => {
            commit("SET_CURRENT_USER", res.data);
          })
          .catch((err) => {
            if (err.response.status === 401) {
              dispatch("removeToken");
              router.push({ name: "login" });
            }
          });
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: "get",
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_PROFILE", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    followUser({ commit, getters }, userPk) {
      axios({
        url: drf.accounts.follow(userPk),
        method: 'put',
        headers: getters.authHeader,
      })
      .then((res) => {
        commit('SET_PROFILE', res.data)
      })
      .catch((err) => {
        console.log(err);
      })
    },
  },
};
