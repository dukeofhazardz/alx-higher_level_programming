#!/usr/bin/node

/*
 * A script that searches the second biggest integer in the list of arguments.
 */

const arg = process.argv.slice(2);

if (arg && arg.length > 1) {
  const newArg = arg.map(arg => parseInt(arg, 10));
  const sortedArg = newArg.sort((a, b) => (b - a));
  console.log(sortedArg[1]);
} else { console.log(0); }
