#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndPoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(movieEndPoint, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const res = await new Promise((resolve, reject) => {
        request(character, (error, res, html) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(res);
    }
  }
});
