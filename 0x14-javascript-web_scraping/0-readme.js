#!/usr/bin/node
const fs = require('fs');
const fToRead = process.argv[2];
fs.readFile(fToRead, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
