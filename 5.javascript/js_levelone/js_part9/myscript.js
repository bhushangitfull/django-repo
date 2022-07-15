var firstname = prompt("First name please")
var lastname = prompt("Last name please")
var age = prompt("How old are your?")
var height = prompt("What is your height in cm")
alert("Tankh you so much for the information")


//four condition

var nameCond = null
var ageCond = null
var heightCond = null

//Name condition

if (firstname[0] === lastname[0]) {
  nameCond = true;
}else {
  nameCond = false
}

//Age condition
if (age>20 && age<30) {
    ageCond = true
}else {
  ageCond = false
}

// Height condition

if(height >= 170){
  heightCond = true
}else {
  heightCond = false
}

// check all conditions
if(nameCond && ageCond && heightCond ){
  alert("welcome spy");
}else {
  alert("something went wrong")
}
