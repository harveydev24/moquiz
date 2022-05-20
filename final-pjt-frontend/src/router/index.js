import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '../views/HomeView.vue'

import CommunityView from '@/views/CommunityView.vue'

import RankingView from '@/views/RankingView.vue'

import ProblemView from '@/views/ProblemView.vue'

import ProFileView from '@/views/ProFileView.vue'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'

import NotFound404 from '../views/NotFound404.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/ranking',
    name: 'ranking',
    component: RankingView
  },
  {
    path: '/problem',
    name: 'problem',
    component: ProblemView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProFileView
  },

  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },

  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
