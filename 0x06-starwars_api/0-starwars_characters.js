#!/usr/bin/node

const request = require('request');
const argument = process.argv[2];
const filmsUrl = 'https://swapi-api.alx-tools.com/api/films/' + argument;

const print_actor_names = (idx, actors) => {
  if (idx === actors.length) return;
  request(actors[idx], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    print_actor_names(++idx, actors);
  });
}

request(filmsUrl, (err, response, body) => {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  print_actor_names(0, actors);
});


