<template>

  <div class="container">
    <!-- Play Header-->
    <div class="notification is-info mt-5">
      Your QuickQuiz for June 25, 20022
    </div>
  </div>

  <div class="container mt-5">
    <div class="box">
      <div class="block">
        <div class="panel is-info">
          <div class="panel-heading">What is the answer?</div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the first answer</label>
            </div>
          </div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the second answer</label>
            </div>
          </div>
          <div class="panel-block">

            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the third answer</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box">
      <div class="block">
        <div class="panel is-info">
          <div class="panel-heading">What is the answer?</div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the first answer</label>
            </div>
          </div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the second answer</label>
            </div>
          </div>
          <div class="panel-block">

            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the third answer</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box">
      <div class="block">
        <div class="panel is-info">
          <div class="panel-heading">What is the answer?</div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the first answer</label>
            </div>
          </div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the second answer</label>
            </div>
          </div>
          <div class="panel-block">

            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the third answer</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box">
      <div class="block">
        <div class="panel is-info">
          <div class="panel-heading">What is the answer?</div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the first answer</label>
            </div>
          </div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the second answer</label>
            </div>
          </div>
          <div class="panel-block">

            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the third answer</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box">
      <div class="block">
        <div class="panel is-info">
          <div class="panel-heading">What is the answer?</div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the first answer</label>
            </div>
          </div>
          <div class="panel-block">
            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the second answer</label>
            </div>
          </div>
          <div class="panel-block">

            <div class="control">
              <input type="radio" id="1">
              <label class="radio">This is the third answer</label>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { inject, onMounted } from 'vue'

export default {
  name: 'Home',
  components: { },
  setup() {
    const store = inject('store')

    onMounted(() => {
      console.log('fetch todays game')
 
    })

    return { store }
  }
}
</script>
