#!/usr/bin/node

const movieid = process.argv[2];

const superagent = require('superagent');

async function getfilms () {
  try {
    const res = await superagent.get(`https://swapi-api.alx-tools.com/api/films/${movieid}`);
    if (res.body && res.body.characters) {
      const characters = res.body.characters;
      for (const character of characters) {
        const result = await superagent.get(character);
        if (result.body && result.body.name) {
          const name = result.body.name;
          console.log(name);
        }
      }
    }
  } catch (err) {
    console.error(err);
  }
}
getfilms();
