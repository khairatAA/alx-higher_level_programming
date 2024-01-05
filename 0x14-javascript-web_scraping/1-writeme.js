#!/usr/bin/node
// 1-writeme

// A script that writes a string to a file.
const fs = require('fs');
const processArgv = require('process').argv;

fs.writeFile(processArgv[2], processArgv[3], err => {
  if (err) {
    console.error(err);
  }
});
