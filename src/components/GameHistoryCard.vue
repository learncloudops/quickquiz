<template>
  <!-- start game -->
  <div class="column is-one-third">
    <div class="card">
      <div class="card-header">
        <div class="card-header-title is-vcentered">
          Played: {{ formatDate }}
        </div>
      </div>
      <div class="card-content">
        <div class="columns">
          <div class="column">
            <figure class="image is-96x96">
              <img :src="link" />
            </figure>
          </div>
          <div class="column is-size-4">{{game.score}} points</div>
        </div>
      </div>
    </div>
  </div>
  <!-- end game -->
</template>


<script>
import { computed } from 'vue'

export default {
  props: ['game'],
  setup(props){
    const formatDate = computed(()=>{
      return props.game.date_played
    })

    const link = computed(()=>{
      const score = props.game.score
      let link = 'images/clown.png'
      if (score <300){
        link = 'images/clown.png'
      }else if(score >= 300 && score <= 400) {
        link = 'images/average.png'
      }else if( score === 500){
        link = 'images/genius.png'
      }

      return link
    })

    return { formatDate, link }
  }
}

</script>