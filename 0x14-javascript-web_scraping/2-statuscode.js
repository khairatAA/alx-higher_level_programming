#!/usr/bin/node
// 2-statuscode.js

// A script that display the status code of a GET request.
const processArgv = require('process').argv;
const request = require('request');

request.get(processArgv[2], function (error, response) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
