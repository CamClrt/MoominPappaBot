import {addDiscussionElement} from './utils.js';
import {send} from './utils.js';

// ---- bot class ---- //

export class Bot {
    constructor(){
        this.type = "bot";
    }

    greetUser(message) {
        // greet user when the page is loading
        const greetingMessage = message;
        document.body.onload = addDiscussionElement(greetingMessage, this.type);
    }

    answer(question) {
        let botResponse = send(question, "/ask_question/");
        if (botResponse.response == "not a question"){
            this.notAQuestion();
        } else {
            addDiscussionElement(botResponse.response, this.type);
        }
    } 

    notAQuestion() {
        const notAQuestionMessage = "Hum... Je ne suis pas sur que cette phrase soit réellement une question... Peux-tu préciser ta pensée ?";
        addDiscussionElement(notAQuestionMessage, this.type);
    }  

    noAnswer() {
        const noAnswerMessage = "Hum ! Il me reste tant à découvrir... Je suis désolé, je ne connais pas ce lieu";
        addDiscussionElement(noAnswerMessage, this.type);
    }

}