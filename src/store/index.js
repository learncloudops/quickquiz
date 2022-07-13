import {reactive,readonly} from 'vue'
import { API } from 'aws-amplify'

const dt = new Date()
const fmtDate = dt.toISOString().split('T')[0]

const state = reactive({
  currentDate: fmtDate,
  username: 'mgivney',
  leaders: [],
  game: {},
  questionIndex: 0,
  playedGames: []
})


// const get = (url) => {
//   API.get('quickquizapi', `/games/played/user/${state.username}`, { })
//      .then(result=>console.log('result', JSON.stringify(result)))
//      .catch(err=>console.log(err))
// }

const methods = {

  async fetchData(){
    
  },


  fetchPlayedGamesByUser(){
    API.get('quickquizapi', `/games/played/user/${state.username}`, {})
        .then(result=>{
          state.playedGames = result.data
        })
        .catch(err=>console.log(err))
  },


  fetchGame(gameDate){
    const game = {
      game_id: '20220712',
      questions: [
        {
          qid: 'd8c6fcbf-e5d2-4911-afb4-6e2b6c906657',
          category: 'General Knowledge',
          type: 'multiple',
          difficulty: 'easy',
          question: 'What kind of aircraft was developed by Igor Sikorsky in the United States in 1942?',
          answers: [ 'Stealth Blimp', 'Helicopter', 'Jet', 'Space Capsule' ]
        },
        {
          qid: 'd8c6fcbf-e5d2-4911-afb4-6e2b6c906657',
          category: 'General Knowledge',
          type: 'multiple',
          difficulty: 'easy',
          question: 'What is the second question?',
          answers: [ 'Stealth Blimp', 'Helicopter', 'Jet', 'Space Capsule' ]
        },
        {
          qid: 'd8c6fcbf-e5d2-4911-afb4-6e2b6c906657',
          category: 'General Knowledge',
          type: 'multiple',
          difficulty: 'easy',
          question: 'What kind of aircraft was developed by Igor Sikorsky in the United States in 1942?',
          answers: [ 'Stealth Blimp', 'Helicopter', 'Jet', 'Space Capsule' ]
        },
        {
          qid: 'd8c6fcbf-e5d2-4911-afb4-6e2b6c906657',
          category: 'General Knowledge',
          type: 'multiple',
          difficulty: 'easy',
          question: 'What kind of aircraft was developed by Igor Sikorsky in the United States in 1942?',
          answers: [ 'Stealth Blimp', 'Helicopter', 'Jet', 'Space Capsule' ]
        },
        {
          qid: 'd8c6fcbf-e5d2-4911-afb4-6e2b6c906657',
          category: 'General Knowledge',
          type: 'multiple',
          difficulty: 'easy',
          question: 'What kind of aircraft was developed by Igor Sikorsky in the United States in 1942?',
          answers: [ 'Stealth Blimp', 'Helicopter', 'Jet', 'Space Capsule' ]
        }
      ]
    }
    state.game = game    
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