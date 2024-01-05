#!/usr/bin/node
// 4-starwars_count.js

// A script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const processArgv = require('process').argv;
const url = processArgv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const responseData = JSON.parse(body);
    const characterUrl = "https://swapi-api.alx-tools.com/api/people/18/";
    let count = 0;

    if (responseData.results) {
      for (let i = 0; i < responseData.results.length; i++) {
	const characters = responseData.results[i].characters;
        if (characters.includes(characterUrl)) {
          count++;
	}
      }
    }
    console.log(count);
  }
});
