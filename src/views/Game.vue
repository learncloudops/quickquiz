<template>

  <!-- <div class="container">
    <div class="notification is-info mt-5">
      Your QuickQuiz for {{ currentDate }}
    </div>
  </div> -->

  <form>
    <div class="container mt-5" v-if="questionIndex < questions.length">
      <!-- Q -->
      <div class="box">
        <div class="block">
          <div class="panel is-info">
            <div class="panel-heading">{{question.question}}</div>
            <input type="hidden" v-model="questionId" />
            <!-- start A-->
            <div class="panel-block" v-for="choice of question.answers" :key="choice">
              <div class="control">
                <label class="radio">
                  <input type="radio" name="choice" v-model="answer" :value="choice">
                  {{choice}}
                </label>
              </div>
            </div>
            <!-- End A-->
          </div>
        </div>
        <button type="button" @click="submit" class="button is-info">Next</button>
      </div>
      <!-- End Q -->
    </div>
    <div v-else>
      <div class="container mt-5">
        <div class="notification is-success">
          <button class="delete"></button>
          You scored a total of {{score * 100}} points this game. Click <a @click="submitScore">here</a> to submit your score for the day.
        </div>
      </div>
    </div>
  </form>
</template>

<script>

const questions =  [
  {
    qid: 'a',
    category: 'General Knowledge',
    type: 'multiple',
    difficulty: 'easy',
    question: 'What kind of aircraft was developed by Igor Sikorsky in the United States in 1942?',
    answers: ['Stealth Blimp', 'Helicopter', 'Jet', 'Space Capsule'],
    rightAnswer: 'Helicopter'
  },
  {
    qid: 'b',
    category: 'General Knowledge',
    type: 'multiple',
    difficulty: 'easy',
    question: 'In the original script of "The Matrix"", the machines used humans as additional computing power instead of batteries.',
    answers: ['True', 'False'],
    rightAnswer: 'True'
  },
  {
    qid: 'c',
    category: 'General Knowledge',
    type: 'multiple',
    difficulty: 'easy',
    question: 'According to their 1974 hit, what were Brownsville Station doing "In The Boys Room"?',
    answers: ['Hangin', 'Smokin', 'Peein', 'Lovin'],
    rightAnswer: 'Smokin'
  },
  {
    qid: 'd',
    category: 'General Knowledge',
    type: 'multiple',
    difficulty: 'easy',
    question: 'When was Chapter 1 of the Source Engine mod &quot;Underhell&quot; released?',
    answers: ['March 3rd, 2011', 'June 5th, 2018', 'September 1st, 2013', 'October 2nd, 2012'],
    rightAnswer: 'September 1st, 2013'
  },
  {
    qid: 'e',
    category: 'General Knowledge',
    type: 'multiple',
    difficulty: 'easy',
    question: 'During World War I, which nation;s monarchs were blood related?',
    answers: ['France, Russia, Germany', 'England, Germany, Russia', 'Germany, Spain, Austria', 'Serbia, Russia, Croatia'],
    rightAnswer: 'England, Germany, Russia'
  }
]

export default {
  name: 'Game',
  components: {},

  data(){
    return {
      currentDate: '2022-07-12',
      questions, 
      questionIndex: 0,
      question:questions[0],
      questionId: questions[0].qid,
      answer: "",
      score: 0,
    }
  },
  methods: {
    submit(){
      // console.log('in submit')
      const { answer, question, questions, questionIndex, questionId } = this

    if(answer=== question.rightAnswer){
        console.log('correct!')
        this.score++
      }

      if(questionIndex < questions.length){
        console.log(questions[questionIndex].qid)
        console.log('Index', questionIndex)
        console.log('Length', questions.length)

        this.question = { ...questions[this.questionIndex] }
        if(this.question){
          this.questionId = questions[this.questionIndex].qid
        }
        this.questionIndex++
      } else {

      }
    },
    submitScore(){
      console.log('submit score')
      console.log('currentDate', this.currentDate)
      console.log('score', this.score)
      this.$router.push({name: 'Home'})
    }
  }
}
</script>
