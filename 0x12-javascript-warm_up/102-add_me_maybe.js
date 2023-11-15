#!/usr/bin/node

// function that increments and calls a function

function addMeMaybe (number, theFunction) {
  return theFunction(number + 1);
}

module.exports.addMeMaybe = addMeMaybe;
