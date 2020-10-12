// ---- function ---- //

// display a new message at screen
let mapIdCounter = 0;
let mapId = "";
export const addDiscussionElement = (text, userType, dataType="text") => {
    const newDiscussionElement = document.createElement("div");
    if (dataType=="url"){
        newDiscussionElement.innerHTML = "<p><a href=".concat(text, " target='_blank'>[En savoir plus sur Wikipedia]</a></p>");
    }
    else if (dataType=="map"){
        mapIdCounter += 1;
        mapId = "map".concat(mapIdCounter);
        newDiscussionElement.setAttribute("id", mapId);
    } else {
        newDiscussionElement.innerHTML = "<p>".concat(text, "</p>");
    };
    newDiscussionElement.classList.add(userType);
    let discussionElement = document.getElementById("discussion");
    discussionElement.appendChild(newDiscussionElement);
    refreshDisplay()
    return mapId;
}

// refresh sreen //
export const refreshDisplay = () => {
    const discussionElement = document.getElementById('discussion');
    const coord = discussionElement.getBoundingClientRect();
    window.scrollTo(0,coord['bottom'])
};

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

// Initialize and add the map
export const initMap = (placeLatitude, placeLongitude, id) => {
    var place = {lat: placeLatitude, lng: placeLongitude};
    var map = new google.maps.Map(document.getElementById(id), {zoom: 10, center: place});
    var marker = new google.maps.Marker({position: place, map: map});
}