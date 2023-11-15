#!/usr/bin/node
//  class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  // a class Square that defines a square

  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let row = '';

      for (let i = 0; i < this.size; i++) {
        row = c.repeat(this.size);
        console.log(row);
      }
    }
  }
};
