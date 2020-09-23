// ---- function ---- //

// display a new message at screen
export const addDiscussionElement = (discussionText, userType) => {
    const newDiscussionElement = document.createElement("div");
    newDiscussionElement.innerHTML = "<p>" + discussionText + "</p>";
    newDiscussionElement.classList.add(userType);
    let discussionElement = document.getElementById("discussion");
    discussionElement.appendChild(newDiscussionElement);
}

// send an HTTP request
export const send = (input, url) => {
    const request = new XMLHttpRequest();
    request.open("POST", url, false);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify({user_question: input}));

    if (request.status == "200") {
        const response = JSON.parse(request.response);
        return response;
    }
}