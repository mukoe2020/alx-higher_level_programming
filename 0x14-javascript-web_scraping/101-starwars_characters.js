#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  const characterUrl = characters[index];
  request(characterUrl, (error, response, body) => {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacters(characters, index + 1);
    }
  });
}
