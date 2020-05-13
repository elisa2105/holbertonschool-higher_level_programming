#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
req.get(url, (error, response, body) => {
  if (!error) {
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
