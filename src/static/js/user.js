import {addDiscussionElement} from "./utils.js";

// ---- user class ---- //

export class User {
    constructor() {
        this.type = "user";
    }

    askQuestion(event) {
        let question = event.target.value;
        return question;
    }

    summitQuestionToBot(question, botObject) {
        if(question !== "") {
            addDiscussionElement(question, this.type);
            botObject.answer(question);
            let userInputElement = document.getElementById("user_question");
            userInputElement.value = "";
        }
    }
}
