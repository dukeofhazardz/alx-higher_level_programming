#!/usr/bin/node

/*
 * A script that concats 2 files.
 */

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destFile = process.argv[4];

const stream1 = fs.createReadStream(file1);
const stream2 = fs.createReadStream(file2);
const destStream = fs.createWriteStream(destFile);

stream1.pipe(destStream);
stream2.pipe(destStream);
