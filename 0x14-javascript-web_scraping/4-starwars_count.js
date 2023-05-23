#!/usr/bin/node
/* A script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */

const url = process.argv[2];

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find(character => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
