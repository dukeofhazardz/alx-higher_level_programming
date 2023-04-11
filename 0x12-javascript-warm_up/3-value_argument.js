#!/usr/bin/node

/*
 * A script that prints the first argument passed to it
 */

import { argv } from 'node:process';

if (argv[2]) {
  console.log(argv[2]);
} else { console.log('No argument'); }
