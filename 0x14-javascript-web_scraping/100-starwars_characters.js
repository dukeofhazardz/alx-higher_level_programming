#!/usr/bin/node
/* A script that prints all characters of a Star Wars movie: */

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let characters = JSON.parse(body).characters;
    for (let character of characters) {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
