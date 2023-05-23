#!/usr/bin/node
/* A script that display the status code of a GET request. */

const url = process.argv[2];

const request = require('request');
request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
