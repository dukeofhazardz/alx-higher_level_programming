#!/usr/bin/node

/*
 * A script that prints the addition of 2 integers
 */

function add(a, b) {
	return parseInt(a) + parseInt(b);
}

const arg = process.argv.slice(2);

console.log(add(arg[0], arg[1]));
