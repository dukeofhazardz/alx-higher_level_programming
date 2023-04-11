#!/usr/bin/node

/*
 * A script that prints a message depending of the number of arguments passed
 */

const argCount = process.argv.length - 2;

if (argCount === 2) {
  console.log('Arguments found');
} else if (argCount === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
