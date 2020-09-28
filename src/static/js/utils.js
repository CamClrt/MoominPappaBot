// ---- function ---- //

// display a new message at screen
export const addDiscussionElement = (discussionText, userType, map=false) => {
    const newDiscussionElement = document.createElement("div");
    if (map==false){
        newDiscussionElement.innerHTML = "<p>".concat(discussionText, "</p>");
    } else {
        newDiscussionElement.setAttribute("id", "map");
    };
    newDiscussionElement.classList.add(userType);
    let discussionElement = document.getElementById("discussion");
    discussionElement.appendChild(newDiscussionElement);
}

// send an HTTP request
export const send = (input, url) => {
    const request = new XMLHttpRequest();
    request.open("POST", url, false);
    request.setRequestHeader("Content-Type", "application/json");
    console.log(JSON.stringify({user_question: input}));
    request.send(JSON.stringify({user_question: input}));

    if (request.status == "200") {
        const response = JSON.parse(request.response);
        return response;
    }
}

// Initialize and add the map
export const initMap = (placeLatitude, placeLongitude) => {
    var place = {lat: placeLatitude, lng: placeLongitude};
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 4, center: place});
    var marker = new google.maps.Marker({position: place, map: map});
}