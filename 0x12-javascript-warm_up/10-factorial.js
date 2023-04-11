#!/usr/bin/node

/*
 * A script that computes and prints a factorial
 */

function factorial (n) {
  if (n < 1) {
    return (1);
  }
  return n * factorial(n - 1);
}

const arg = process.argv.slice(2);

console.log(factorial(parseInt(arg[0])));
