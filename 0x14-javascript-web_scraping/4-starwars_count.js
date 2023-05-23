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
    const characters = result[1].characters;

    const character = characters.find(link => link.endsWith('/18/'));

    request(character, function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        const noFilms = JSON.parse(body).films.length;
        console.log(noFilms);
      }
    });
  }
});
