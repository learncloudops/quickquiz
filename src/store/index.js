import {reactive,readonly} from 'vue'
import { API } from 'aws-amplify'

const state = reactive({
  username: 'mgivney',
  leaders: [],
  game: {},
  playedGames: []
})


const get = (url) => {
  API.get('quickquizapi', `/games/played/user/${state.username}`, { })
     .then(result=>console.log('result', JSON.stringify(result)))
     .catch(err=>console.log(err))
}

const methods = {

  fetchPlayedGamesByUser(){
    API.get('quickquizapi', `/games/played/user/${state.username}`, {})
        .then(result=>{
          state.playedGames = result.data
        })
        .catch(err=>console.log(err))
  },

  /** Game Actions */
  getGameByDate(gameDate){

  },

  getGamesByUser(){
    const uri = `/games/users/${this.state.username}`
    API.get('quickquizapi', uri, {})
        .then(result => {
          console.log('result', JSON.stringify(result))
        })
        .catch(err => console.log(err))

  },

  saveGame(game){
  },

  /** Questions */
  getQuestionById(id){
    return {}
  },

  /** leaders */
  getAllTimeLeaders(){
  },

  getMonthlyLeaders(month){
  }

}

export default {
  state: readonly(state),
  methods

}