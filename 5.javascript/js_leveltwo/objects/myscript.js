//1.Add method called namelength that prints out the lenght of the employee
// var employee = {
//   name: "John Smith",
//   job: "Programmer",
//   age: 31,
//   namelength: function () {
//     console.log(this.name.length);
//   }
// }


//2.write  program that will create an alert in the browser
//of each of the object's values for the key value pairs.

var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  report: function() {
    alert("name is "+this.name+",job is: "+this.job+", Age is : "+this.age)
  }
}

employee.report()

//3.add a method called  lastname that prints out the employees last name
// var employee = {
//   name: "John Smith",
//   job: "Programmer",
//   age: 31,
//   lastName: function () {
//     console.log(this.name.split("")[1]);
//   }
// }
