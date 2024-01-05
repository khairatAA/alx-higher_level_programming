#!/usr/bin/node
// 0-readme module

// A script that reads and prints the content of a file
const fs = require('fs');
const processArgv = require('process').argv;

fs.readFile(processArgv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
