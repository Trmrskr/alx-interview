#!/usr/bin/node

const request = require('request');
const argument = process.argv[2];
const filmsUrl = 'https://swapi-api.alx-tools.com/api/films/' + argument;

const printActorNames = (idx, actors) => {
  if (idx === actors.length) return;
  request(actors[idx], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    printActorNames(++idx, actors);
  });
};
request(filmsUrl, (err, response, body) => {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  printActorNames(0, actors);
});


