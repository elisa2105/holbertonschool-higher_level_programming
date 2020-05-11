#!/usr/bin/node
const SquareG = require('./5-square');

const Square = class extends SquareG {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
module.exports = Square;
