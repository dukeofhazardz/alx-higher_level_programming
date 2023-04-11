#!/usr/bin/node

/*
 * A script that prints two arguments passed to it, in the
 * following format: “ is ”
 */

import { argv } from 'node:process';

console.log(argv[2] + ' is ' + (argv[3]));
