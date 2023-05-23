#!/usr/bin/node
/* A script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
