#!/usr/bin/node
/* A script that prints all characters of a Star Wars movie:
 * Displaying one character name by line in the same order of
 * the list “characters” in the /films/ response
 */

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    const promises = [];
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
    Promise.all(promises).then((a) => {
      for (const i of a) { console.log(i); }
    });
  }
});
