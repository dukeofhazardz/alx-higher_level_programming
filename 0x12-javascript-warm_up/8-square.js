#!/usr/bin/node

/*
 * A script that prints a square
 */

const size = parseInt(process.argv.slice(2));

if (size && Number.isInteger(size)) {
	for (let i = 0; i < size; i++) {
		let row = '';
		for (let j = 0; j < size; j++) {
			row += 'X';
		}
		console.log(row);
	}
}
else
	console.log('Missing size');
