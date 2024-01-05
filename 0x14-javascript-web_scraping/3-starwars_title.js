#!/usr/bin/node
// 3-starwars_title.js

// A script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const processArgv = require('process').argv;
const url = `https://swapi-api.alx-tools.com/api/films/${processArgv[2]}`;

request.get(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const responseData = JSON.parse(body);
    console.log(responseData.title);
  }
});
