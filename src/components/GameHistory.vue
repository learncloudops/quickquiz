<template>
  <div class="container ">
    <div class="columns mt-5 is-multiline">
      <GameHistoryCard v-for="game in games" :key="game.id" :game="game"/>
    </div>
  </div>
</template>

<script>
import GameHistoryCard from './GameHistoryCard.vue'

export default {
  props: ['games'],
  components: { GameHistoryCard }
}
</script>
