#!/usr/bin/node

const fileSystem = require('fs');
const fToWrite = process.argv[2];
const textToWrite = process.argv[3];
fileSystem.writeFile(fToWrite, textToWrite, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  }
});
