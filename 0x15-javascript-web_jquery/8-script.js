// fetches and lists the title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const results = data.results;

  for (let i = 0; i < results.length; i++) {
    $('#list_movies').append(`<li>${results[i].title}</li>`);
  }
});
