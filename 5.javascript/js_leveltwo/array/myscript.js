//create empty student roster array
var roster = []

//create the functions for the the tasks


//ADD a new student function

function addNew() {
  var newName = prompt("What name would you like to add?")
  roster.push(newName)
}


//Remove student function

function remove() {
  var remName = prompt("what name would you like to remove")
  var index = roster.indexOf(remName)
  roster.splice(index,1)
}

//display roster function

function display() {
  alert(roster)
}

//start the roste webapp

var start = prompt("Would you like to start the roaster web app? y/n")
var request = "empty"

if (start === 'y') {
    while (request !== "quit") {
        request = prompt("Please select the action: add, remove, display, or quit.")
        if (request ==='add') {
          addNew()
        }else if (request === 'remove') {
            remove()
        }else if (request === 'display') {
            display()
        }
        else {

          request = 'quit'
        }
    }
}
alert("Thanks for using the wep app")
