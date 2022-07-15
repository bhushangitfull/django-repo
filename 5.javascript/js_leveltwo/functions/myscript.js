function formal(name="same", title="sir") {

  return title+" " +name

}


function timesfive(numInput) {
    var result = numInput * 5
    return result;
}

//Global scope
var v = "Global V"
var stuff = "Global Stuff"

function func(stuff) {
    console.log(v);
    stuff = "Reassign stuff inside func"
    console.log(stuff);
}

func()
