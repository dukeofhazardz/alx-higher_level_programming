#!/usr/bin/node
/* A script that computes the number of tasks completed by user id. */

const url = process.argv[2];

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < result.length; i++) {
      if (result[i].completed === true) {
        const key = String(result[i].userId);
        dict[key] = (dict[key] || 0) + 1;
      }
    }
    console.log(dict);
  }
});
