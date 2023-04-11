#!/usr/bin/node

/*
 * A script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */

const num = process.argv[2];

if (isNaN(num) && !Number.isInteger(num)) {
  console.log('Not a number');
} else { console.log('My number: ' + parseInt(num)); }
