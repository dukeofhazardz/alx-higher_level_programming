#!/usr/bin/node

/*
 * A script that prints a message depending of the number of arguments passed
 */

import { argv } from 'node:process';

if (argv[3]) {
  console.log('Arguments found');
} else if (argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
