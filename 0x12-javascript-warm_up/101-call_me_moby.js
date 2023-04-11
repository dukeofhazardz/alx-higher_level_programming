#!/usr/bin/node

/*
 * A function that executes x times a function.
 */

exports.callMeMoby = function (num, theFunction) {
  for (let i = 0; i < num; i++) {
    theFunction();
  }
};
