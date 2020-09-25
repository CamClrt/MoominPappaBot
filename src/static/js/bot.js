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
        } else if (botResponse.response == "nothing"){
            this.noAnswer();
        } else {
            addDiscussionElement(botResponse.response, this.type);
        }
    } 

    notAQuestion() {
        const response = "Hum... Je ne suis pas sur que cette phrase soit réellement une question... Peux-tu reformuler sous forme de question ?";
        addDiscussionElement(response, this.type);
    }  

    noAnswer() {
        const response = "Hum ! Il me reste tant de chose à découvrir... Je suis désolé, je ne connais pas ce lieu. N'hésites pas à vérifier son orthographe et s'il porte des majuscules !";
        addDiscussionElement(response, this.type);
    }
}
