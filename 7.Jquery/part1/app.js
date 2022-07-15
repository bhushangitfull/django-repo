

/*$('h1').click(function () {
  $(this).text("Hi!")
})*/

//Kwy Press

$('input').eq(0).keypress(function (event) {

      $('p').eq(0).toggleClass('turnRed')

})

//on()

$('h1').on('mouseenter',function () {
  $(this).toggleClass('turnBlue')
})

//animation

$('input').eq(1).on('click',function() {
  $('.demo').fadeOut(1000)
})
