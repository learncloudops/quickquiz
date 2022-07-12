
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { Amplify } from 'aws-amplify'
import awsConfig from './aws-exports'
import '@aws-amplify/ui-vue/styles.css'

Amplify.configure(awsConfig)

createApp(App).use(router).mount('#app')
