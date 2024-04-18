#!/usr/bin/node

const movieid = process.argv[2];

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request(url, function (error, response, body) {
  if (error == null) {
    const res = JSON.parse(body);
    const characters = res.characters;
    getNames(characters, 0);
  }
});

function getNames (characters, idx) {
  request(characters[idx], function (error, response, body) {
    if (error == null) {
      const res = JSON.parse(body);
      const name = res.name;
      console.log(name);
      if (idx < characters.length - 1) {
        getNames(characters, idx + 1);
      }
    }
  });
}
