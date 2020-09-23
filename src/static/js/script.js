// ---- function ---- //

// display a new message at screen
const addDiscussionElement = (discussionText, classeName) => {
    const newDiscussionElement = document.createElement("div");
    newDiscussionElement.innerHTML = "<p>" + discussionText + "</p>";
    newDiscussionElement.classList.add(classeName);
    let discussionElement = document.getElementById("discussion");
    discussionElement.appendChild(newDiscussionElement);
}

// send an HTTP request
const send = (input, url) => {
    const request = new XMLHttpRequest();
    request.open("POST", url, false);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify({user_question: input}));

    if (request.status == "200") {
        const response = JSON.parse(request.response);
        return response
      }
}

// ------------------ //

// greet user when the page is loading
const greetingMessage = "Bonjour à toi aventurier ! De quel lieu souhaites-tu que je te parle ?"
document.body.onload = addDiscussionElement(greetingMessage, "bot");

// user ask a question and receive a response to the bot 
let userInputResult = "";
let userInputElement = document.getElementById("user_question");
    userInputElement.addEventListener('change', function(event) {
        userInputResult = event.target.value;
});

const buttonElement = document.getElementById("button");
buttonElement.addEventListener("click", function(){
    
    if(userInputElement.value != "") {
        addDiscussionElement(userInputResult, "user");
        let botResponse = send(userInputResult, "/ask_question/");
        // and user receive a response
        addDiscussionElement(botResponse.response, "bot");
        userInputElement.value = "";
    };
});