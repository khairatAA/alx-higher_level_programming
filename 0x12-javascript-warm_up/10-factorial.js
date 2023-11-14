#!/usr/bin/node

// a script that computes and prints a factorial

function factorial (num) {
  const numInt = parseInt(num);

  if (isNaN(num) || numInt < 0) {
    return 1;
  } else if (numInt === 0) {
    return 1;
  } else {
    return numInt * factorial(numInt - 1);
  }
}

const result = factorial(process.argv[2]);
console.log(result);
