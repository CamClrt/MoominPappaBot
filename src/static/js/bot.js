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
            addDiscussionElement(botResponse.response, this.type);
    }

    noQuestion() {
        const noQuestionMessage = "Voyons, ne soit pas timide ! N'hésites pas à me poser ta question...";
        addDiscussionElement(noQuestionMessage, this.type);
    }

    noAnswer() {
        const noAnswerMessage = "Hum ! Il me reste tant à découvrir... Je suis désolé, je ne connais pas ce lieu";
        addDiscussionElement(noAnswerMessage, this.type);
    }

}