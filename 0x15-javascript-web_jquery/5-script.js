// adds a <li> element to a list when the user clicks on the tag DIV#add_item

$('#add_item').on('click', function () {
    $('<li>Item</li>').appendTo('.my_list')
  });