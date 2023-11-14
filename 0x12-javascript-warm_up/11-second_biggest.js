#!/usr/bin/node

// A script that searches the second biggest integer in the list of arguments

const entries = process.argv.slice(2);
let max = 0;

// entries.forEach((val, index) => {
// console.log(`${index}: ${val}`);
// });

if (entries.length === 0) {
  max = 0;
  console.log(max);
} else if (entries.length === 1) {
  max = 0;
  console.log(max);
} else {
  for (let i = 0; i < entries.length; i++) {
    const num1 = parseInt(entries[i]);
    if (num1 > max) {
      max = num1;
    }
  }
  console.log(max);
}
