import {addDiscussionElement} from './utils.js';
import {send} from './utils.js';
import {initMap} from './utils.js';

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
             // add name of the place
            this.giveTheNamePlace(botResponse.response)
            // add short description
            this.giveTheDescriptionPlace(botResponse.description)
            // add map to locate the place
            this.giveMapPlace(botResponse.latitude, botResponse.longitude)
        }
    } 

    giveTheNamePlace(name) {
        const message = "Oh bien sur ! Tu veux parler de "
        addDiscussionElement(message.concat(name, " !"), this.type);
    }

    giveTheDescriptionPlace(description) {
        const message = "Selon mes sources, voici ce que je peux t'en dire: "
        addDiscussionElement(message.concat(description), this.type);
    }

    giveMapPlace(latitude, longitude) {
        const mapId = addDiscussionElement("", this.type, true)
        initMap(latitude, longitude, mapId)
    }

    notAQuestion() {
        const response = "Hum... Je ne suis pas sur que cette phrase soit réellement une question... Peux-tu reformuler ?";
        addDiscussionElement(response, this.type);
    }  

    noAnswer() {
        const response = "Hum ! Il me reste tant de chose à découvrir... Je suis désolé, je ne connais pas ce lieu. N'hésites pas à vérifier son orthographe et s'il porte des majuscules !";
        addDiscussionElement(response, this.type);
    }
}
