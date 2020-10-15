import { User } from './user.js'
import { Bot } from './bot.js'

// ---- main script ---- //

// greet user
function greetUser () {
  const bot = new Bot()
  const message = ('Bonjour à toi aventurier ! Sur quel lieu souhaites-tu m\'interroger ?')
  bot.greetUser(message)
}

greetUser()

// ask question
const userInputElement = document.getElementById('user_question')

userInputElement.addEventListener('change', inputEvent => {
  const buttonElement = document.getElementById('button')
  buttonElement.addEventListener('click', buttonEvent => {
    const user = new User()
    const bot = new Bot()
    let question = user.askQuestion(inputEvent)
    user.summitQuestionToBot(question, bot)
    question = ''
  })
})

userInputElement.addEventListener('keyup', event => {
  if (event.keyCode === 13) {
    const user = new User()
    const bot = new Bot()
    let question = user.askQuestion(event)
    user.summitQuestionToBot(question, bot)
    question = ''
  }
})
