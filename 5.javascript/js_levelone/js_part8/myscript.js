/////////////////////
///// problem1 /////
////////////////////

//Use a for loop to print console.log out the word "hello" 5 times

//Do this with a while loop and for loop

//while loop:

var x = 0;

while (x<5) {
  console.log("hello");
  x++
}


//for loop

for (var i = 0; i <5 ; i++) {
    console.log("hello with for loop");
}



//////////////////////
/////// Problem2//////
//////////////////////

//use loops to console.log() all the odd numbers from 1 to 25
//do this using two methods, a while loop and a for loops

//method console
//while loops

var num =1

while (num<25) {
  if (num%2!==0) {
      console.log(num);
  }

  num++

}


for (var i = 0; i < 25; i++) {
  if (i%2!==0) {
      console.log(i);
  }
}
