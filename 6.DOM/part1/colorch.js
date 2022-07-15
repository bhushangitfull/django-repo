//Grab the header with h1

var header = document.querySelector("h1")


//Then you can interface with the object.

//interface with the style.



//Random color function:

function getRandomColor() {
  var letters = "0123456789ABCDEF"
  var color = '#'
  for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random()*16)]
  }
  return color;
}

function changeHeaderColor() {
  var colorInput = getRandomColor()
  header.style.color = colorInput
}

//performing the interval action (milliseconds):

setInterval("changeHeaderColor()",300)
