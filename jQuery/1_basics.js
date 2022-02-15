// to check wheather jQuery is working or not
$

// getElementsByTagName('tagName') : functionality
$('h1')
$('li')

// editing CSS style
var x = $('h1')
x.css('color','red')
x.css('background','blue')

// creating object
var newCSS = {
  'color':'white',
  'background':'green',
  'border':'20px solid red'
}
// apply all css styling @ once via object
x.css(newCSS)

// to grab only single list items
var listItems = $('li')
// eq(index)
listItems.eq(0).css('color','orange')
listItems.eq(-1).css('color','orange') // last li

$('h1').text("Changing Text!")
$('h1').html(<em>Changing Text !</em>) // editing HTML

// convert submit button to checkbox
$('input').eq(1).attr('type','checkbox')
// change value of placeholder
$('input').eq(0).val('new-placeholder!')

// add a class with jQuery
$('h1').addClass('turnRed')
// remove a class with jQuery
$('h1').removeClass('turnRed')
// toggle class
$('h1').toggleClass('turnBlue')
