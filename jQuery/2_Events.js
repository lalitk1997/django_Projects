// events
$('h1').click(function(){
  console.log("There was a click !")
  $(this).text("I was changed!")
})

$('li').click(function(){
  console.log("Any li tag is clicked !")
})

$('h2').dblclick(function(){
  console.log("Double Clicked !")
})

// key press
$('input').eq(0).keypress(function(){
  //$('h3').toggleClass('turnBlue')
  console.log(event) // object based on key pressed
  if(event.which === 13){
    $('h3').toggleClass('turnBlue')
  }
})

// on function
// $('h1').on('dblclick', function(){
//   $(this).toggleClass('turnRed');
// })

$('h1').on('mouseenter', function(){
  $(this).toggleClass('turnRed');
})

$('input').eq(1).on('click', function(){
  // $('.container').fadeOut(300)
  $('.container').slideUp(300)
})
