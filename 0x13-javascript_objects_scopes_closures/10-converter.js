#!/usr/bin/node

// converts a number from base 10 to another base passed as argument

exports.converter = function (base) {
  return function convert (number) {
    return (number.toString(base));
  };
};
