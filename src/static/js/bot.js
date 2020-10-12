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
        if (botResponse.response == "nothing"){
            this.noAnswer();
        } else {
            // add short description
            if (botResponse.description != "") {
                this.giveTheDescriptionPlace(botResponse.description)
            }
            // add map to locate the place
            if ((botResponse.latitude, botResponse.longitude) != ("", "")) {
                this.giveMapPlace(botResponse.latitude, botResponse.longitude)
            }
            // add wikipedia url
            if (botResponse.url != "") {
            this.giveUrl(botResponse.url)
            }
        }
    }

    giveTheDescriptionPlace(description) {
        const message = "Selon mes sources, voici ce que je peux t'en dire: "
        addDiscussionElement(message.concat(description), this.type);
    }

    giveMapPlace(latitude, longitude) {
        const mapId = addDiscussionElement("", this.type, "map")
        initMap(latitude, longitude, mapId)
    }

    giveUrl(url) {
        addDiscussionElement(url, this.type, "url");
    }

    noAnswer() {
        const response = "Hum ! Il me reste tant de chose à découvrir... Je ne suis pas sûr de la réponse, tu pourrais peut-être reformuler ta question ?";
        addDiscussionElement(response, this.type);
    }
}
