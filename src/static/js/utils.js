// ---- function ---- //

// display a new message at screen
let mapIdCounter = 0
let mapId = ''
export function addDiscussionElement (text, userType, dataType = 'text') {
  const newDiscussionElement = document.createElement('div')
  const newParagraphBlock = document.createElement('p')
  newDiscussionElement.appendChild(newParagraphBlock)
  if (dataType === 'url') {
    const newUrlElement = document.createElement('a')
    newParagraphBlock.appendChild(newUrlElement)
    newUrlElement.setAttribute('href', text)
    newUrlElement.setAttribute('target', '_blank')
    newUrlElement.textContent = '[En savoir plus sur Wikipedia]'
  } else if (dataType === 'map') {
    mapIdCounter += 1
    mapId = 'map'.concat(mapIdCounter)
    newDiscussionElement.setAttribute('id', mapId)
  } else {
    newParagraphBlock.textContent = text
  }
  newDiscussionElement.classList.add(userType)
  const discussionElement = document.getElementById('discussion')
  discussionElement.appendChild(newDiscussionElement)
  refreshDisplay()
  return mapId
}

// refresh sreen //
export function refreshDisplay () {
  const socialElement = document.getElementById('social_media')
  socialElement.scrollIntoView()
}

// send an HTTP request
export function send (input, url) {
  const request = new XMLHttpRequest()
  request.open('POST', url, false)
  request.setRequestHeader('Content-Type', 'application/json')
  request.send(JSON.stringify({ user_question: input }))

  if (request.status === 200) {
    const response = JSON.parse(request.response)
    return response
  }
}

// Initialize and add the map
export function initMap (placeLatitude, placeLongitude, id) {
  var place = { lat: placeLatitude, lng: placeLongitude }
  var map = new google.maps.Map(document.getElementById(id), { zoom: 10, center: place })
  var marker = new google.maps.Marker({ position: place, map: map })
}
