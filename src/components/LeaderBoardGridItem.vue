<template>
  <div class="panel-block">
    <span class="icon" v-if="showIcon">
      <i class="fa-solid fa-medal"></i>
    </span>
    <span :class="rankColor">{{stat.fname}} {{stat.lname}}</span>
    <span class="px-3">{{stat.score}} points</span>
  </div>
</template>


<script>
import { computed } from 'vue'

export default {
  props: ['stat'],
  setup(props){
    const showIcon = computed(()=>{
      const rank = props.stat.rank
      return rank===1 || rank===2 || rank===3
    })

    const rankColor = computed(()=>{
      const rank = props.stat.rank
      let color = 'has-text-dark'
      
      if(rank===1){
        color = 'has-text-primary-dark' 
      }else if(rank===2){
        color = 'has-text-info-dark'
      }else if(rank===3){
        color = 'has-text-danger'
      }
      return color
    })

    return { showIcon, rankColor }
  }

}
</script>