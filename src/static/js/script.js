import {User} from './user.js';
import {Bot} from './bot.js';

// ---- main script ---- //

let bot = new Bot();
let user = new User();

// greet user
let message = "Bonjour à toi aventurier ! De quel lieu souhaites-tu que je te parle ?";
bot.greetUser(message);

// user ask a question
const userInputElement = document.getElementById("user_question");
userInputElement.addEventListener('change', function(event) {
    let question = user.askQuestion(event);
    const buttonElement = document.getElementById("button");
        buttonElement.addEventListener("click", function(){
            user.summitQuestionToBot(question, bot);
            question = "";
        })
})