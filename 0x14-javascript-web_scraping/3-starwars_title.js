#!/usr/bin/node
const req = require('request');
// const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(url, (error, response, body) => {
  if (error) { console.log(error); } else {
    const e = JSON.parse(body);
    console.log(e.title);
  }
});
