// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and
// displays the value of hello from that fetch in the HTML tag DIV#hello

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const value = data.hello;

  $('#hello').append(value);
});
