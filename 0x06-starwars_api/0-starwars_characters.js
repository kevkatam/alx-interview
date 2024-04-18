#!/usr/bin/node

const movieid = process.argv[2];

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request(url, function (error, response, body) {
  if (error == null) {
    const res = JSON.parse(body);
    const characters = res.characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error == null) {
          const result = JSON.parse(body);
          const name = result.name;
          console.log(name);
        }
      });
    }
  }
});
