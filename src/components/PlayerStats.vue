<template>
  <!-- Start Stats -->
  <div class="box">
    <div class="block">
      <div class="panel is-dark">
        <div class="panel-heading">Your Stats</div>
        <div class="panel-block">
          <span class="has-text-primary-dark">Your Rank</span>
          <span class="px-3">{{playerStats.title}}</span>
        </div>

        <div class="panel-block">
          <span class="has-text-primary-dark">Games played </span>
          <span class="px-3">{{playerStats.totalGames}}</span>
        </div>
        <div class="panel-block">
          <span class="has-text-primary-dark">Today's Points Earned </span>
          <span class="px-3">{{playerStats.todaysPoints}}</span>
        </div>
        <div class="panel-block">
          <span class="has-text-primary-dark">All Time Points Earned</span>
          <span class="px-3">{{playerStats.totalPoints}}</span>
        </div>
      </div>
    </div>
  </div>
  <!-- End Stats -->
</template>

<script>

export default {
  props: ['playerStats']
}
</script>