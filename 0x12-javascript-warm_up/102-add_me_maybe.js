#!/usr/bin/node

/*
 * A function must be visible from outside
 */

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
