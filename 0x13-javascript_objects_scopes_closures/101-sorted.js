#!/usr/bin/node

/*
 * A script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence.
 */

const { dict } = require('./101-data');

const newDict = {};

for (const [userId, occurance] of Object.entries(dict)) {
  if (occurance in newDict) {
    newDict[occurance].push(userId);
  } else {
    newDict[occurance] = [userId];
  }
}

console.log(newDict);
