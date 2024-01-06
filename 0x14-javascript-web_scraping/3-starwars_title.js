#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = `http://swapi.co/api/films/${filmId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const filmTitle = JSON.parse(body).title;
    console.log(filmTitle);
  }
});
