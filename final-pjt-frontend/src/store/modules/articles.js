import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    articles: [],
    article: {},
  },

  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.articles.article?.user === getters.currentUser.user
    },
    isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments.comments),
  },

  actions: {
    fetchArticles({ commit, getters }) {

      axios({
        url: drf.community.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_ARTICLES', res.data)})
        .catch(err => console.error(err.response))
    },

    fetchArticle({ commit, getters }, articlePk) {

      axios({
        url: drf.community.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)})
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    createArticle({ commit, getters }, article) {
      axios({
        url: drf.community.articles() + 'article/',
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    deleteArticle({ commit, getters }, articlePk) {
      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.community.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'community' })
          })
          .catch(err => console.error(err.response))
      }
    },

    likeArticle({ commit, getters }, articlePk) {
      axios({
        url: drf.community.likeArticle(articlePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)})
        .catch(err => {console.error(err.response)
        })
    },

		createComment({ commit, getters }, { articlePk, content }) {
      const comment = { content }

      axios({
        url: drf.community.comments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => {
          console.error(err.response)})
    },

    deleteComment({ commit, getters }, { articlePk, commentPk }) {
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.community.comment(articlePk, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_ARTICLE_COMMENTS', res.data)
            })
            .catch(err => {
              console.error(err.response)})
        }
      },
  },
}
