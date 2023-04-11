#!/usr/bin/node

/*
 * A script that prints the first argument passed to it
 */

import { argv } from 'node:process';

const argument = process.argv.slice(2);

if (argument[0]) {
  console.log(argument[0]);
} else { console.log('No argument'); }
