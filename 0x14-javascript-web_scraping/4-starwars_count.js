#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url, (error, response, body) => {
  if (error) { console.log(error); } else {
    const list = JSON.parse(body).results;
    const characters = [];
    let count = 0;
    for (let i = 0; i < list.length; i++) {
      characters.push(list[i].characters);
    }
    for (let j = 0; j < characters.length; j++) {
      if (String(characters[j]).includes('/18/')) {
        count = count + 1;
      }
    }
    console.log(count);
  }
});
