#!/usr/bin/node

// converts a number from base 10 to another base passed as argument

exports.converter = function (base) {
  return function convert (number) {
    let str = '';

    if (number === 0) {
      return '0';
    }

    while (number > 0) {
      str = number % base + str;
      number = Math.floor(number / base);
    }

    return str;
  };
};
