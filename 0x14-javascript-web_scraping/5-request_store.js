#!/usr/bin/node
/* A script that gets the contents of a webpage and stores it in a file. */

const url = process.argv[2];
const file = process.argv[3];

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = body;
    const fs = require('fs');

    fs.writeFile(file, result, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
