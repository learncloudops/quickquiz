<template>
  <div class="box">
    <div class="block">
      <div class="panel is-dark">
        <div class="panel-heading">{{title}}</div>
        <LeaderBoardGridItem v-for="stat in stats" :key="stat.id" :stat="stat" />
      </div>
    </div>
  </div>
</template>

<script>
import LeaderBoardGridItem from './LeaderBoardGridItem.vue'

export default{
  name: 'LeaderBoardGrid',
  props: ['stats', 'title'],
  components: { LeaderBoardGridItem }
}
</script>