#!/usr/bin/node

/*
 * A class Square that defines a square and inherits from
 * Square of 5-square.js:
 */

class Square extends require('./5-square') {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        let rows = '';
        for (let j = 0; j < this.width; j++) {
          rows += 'C';
        }
        console.log(rows);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
