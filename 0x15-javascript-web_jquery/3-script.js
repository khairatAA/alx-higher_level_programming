// updates the text color of the <header> element to red (#FF0000)
// when the user clicks on the tag DIV#red_header

$('#red_header').on('click', function () {
  $('header').addClass('red');
});
