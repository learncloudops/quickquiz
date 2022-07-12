<template>
  <PlayHeader />
  <GameHistory :games="store.state.playedGames" />
</template>

<script>
import { inject, onMounted } from 'vue'
import GameHistory from '../components/GameHistory.vue'
import PlayHeader from '../components/PlayHeader.vue'

export default {
  name: 'Home',
  components: { GameHistory, PlayHeader },
  setup() {
    const store = inject('store')

    onMounted(() => {
      console.log('fetching played games...')
      store.methods.fetchPlayedGamesByUser()
    })

    return { store }
  }
}
</script>
