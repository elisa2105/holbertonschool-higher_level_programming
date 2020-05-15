/* let count = 0;
$("DIV#toggle_header").click(function() {
    if(count % 2 === 0){
    $("HEADER").css("color", "#FF0000");
    console.log(count);
    }
    else{
    $("HEADER").css("color", "#00FF00");
    console.log(count);
    }
    count++;
}); */

$('DIV#toggle_header').click(function () {
  $('HEADER').toggleClass('green red');
});
