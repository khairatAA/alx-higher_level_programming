#!/usr/bin/node

// prints the addition of 2 integers

function add (a, b) {
  const aNum = parseInt(a);
  const bNum = parseInt(b);

  const sum = aNum + bNum;
  console.log(sum);
}

add(process.argv[2], process.argv[3]);
