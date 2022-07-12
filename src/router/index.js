import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import LeaderBoard from '../views/LeaderBoard.vue'
import Game from '../views/Game.vue'
import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/leaderboard',
    name: 'LeaderBoard',
    component: LeaderBoard
  },
  {
    path: '/game',
    name: 'Game',
    component: Game
  },

  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
