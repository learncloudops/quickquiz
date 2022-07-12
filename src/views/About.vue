<template>
  <div class="container">
    <h1 class="is-size-2">Test this bitch!</h1>
    <button @click="played_by_user">Played Games By User</button>
    <button @click="played_by_date">Played Games By Date</button>
    <button @click="game_by_date">Game By Date</button>
    <button @click="save_game">Save Game</button>
    <button @click="save_played_game">Saved Played Game</button>
    <button @click="fetch_played_by_user_from_store">Fetch Played Games By User from Store</button>

  </div>
</template>

<script>
import { API } from 'aws-amplify'
import { inject } from 'vue'

export default {
  setup(){

    const store = inject('store')

    const get = (url) => {
      API.get('quickquizapi', url, {
      })
          .then(result=>console.log('result', JSON.stringify(result)))
          .catch(err=>console.log(err))
    }
  
    const fetch_played_by_user_from_store = ()=>{
      const data = store.methods.fetchPlayedGamesByUser()
      console.log(store.state.playedGames[0].score)
    }

    const played_by_user = () =>{get('/games/played/user/mgivney')}
    const played_by_date = () => {get('/games/played/date/20220711')}
    const game_by_date = () => {get('/games/20220711')}
    const save_game = () => {}
    const save_played_game = () => {}

    return {
      played_by_date,
      played_by_user,
      game_by_date,
      save_game,
      save_played_game,
      fetch_played_by_user_from_store
    }
  }
}


</script>
