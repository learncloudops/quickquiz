<template>
  <Authenticator variation="modal" v-slot="{ signOut }">

    <nav class="navbar is-dark">
      <div class="navbar-item is-size-3">
        <router-link class="has-text-light" to="/">Quick Quiz</router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <router-link class="has-text-light" to="/game">Play!</router-link>
        </div>
        <div class="navbar-item">
          <router-link class="has-text-light" to="/leaderboard">LeaderBoards</router-link>
        </div>
        <div class="navbar-item">
          <button class="button is-dark" @click="logout">Logout</button>
        </div>
      </div>
    </nav>
    <!--
      <button @click="signOut">Sign Out</button>
    -->
    <router-view />
  </Authenticator>
</template>


<script>
import {provide} from 'vue'
import store from '@/store'
import {Authenticator} from '@aws-amplify/ui-vue'

export default { 
  name: 'App',
  components: {
    Authenticator
  },
  setup(){
      provide('store', store)

      const logout = () =>{
        console.log('log me out fool')
      }


      return { logout }
  }
}

</script>