//alert("Welcome to weight conversion app!")
//
//var weight_lb = prompt("Enter the weight in pounds (lbs): ")
//alert("You entered: " + weight_lb)
//var weight_kg = weight_lb*0.454
//alert(weight_lb + " lb = " + weight_kg + " kg")
//console.log("Conversion complete!")

$('h1').click(function(){
//    console.log('There was a click!')
    $(this).text('I was changed!')
})

$('li').click(function(){
    console.log('Any li was clicked');
})

$('input').eq(0).keypress(function(event){
    if (event.which === 13) {
        $('h3').toggleClass('turnBlue')
    }
//    console.log(event);
//    $('h3').toggleClass('turnBlue');
})

//$('h1').on('dblclick', function(){
//    $(this).toggleClass('turnBlue')
//})

$('h1').on('mouseenter', function(){
    $(this).toggleClass('turnBlue')
})

$('input').eq(1).on('click', function(){
    $('.container').fadeOut(3000)
})