#!/usr/bin/node

/*
 * A script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */

import { argv } from 'node:process';

const num = parseInt(argv[2]);

if (typeof num !== 'number' || !Number.isInteger(num)) {
  console.log('Not a number');
} else { console.log('My number: ' + num); }
