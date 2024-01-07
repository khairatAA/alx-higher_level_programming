#!/usr/bin/node
// 5-request_store.js

// Gets the contents of a webpage and stores it in a file
const request = require('request');
const processArgv = require('process').argv;
const fs = require('fs');

request(processArgv[2], function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(
      processArgv[3],
      body,
      { encoding: 'utf-8' },
      (err) => {
        if (err) throw err;
      }
    );
  }
});
