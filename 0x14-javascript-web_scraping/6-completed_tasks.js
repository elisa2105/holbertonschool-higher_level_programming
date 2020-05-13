#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dictu = {};
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const AllTasks = JSON.parse(body);
    for (let i = 0; i < AllTasks.length; i++) {
      const key = AllTasks[i].userId;
      if (AllTasks[i].completed) {
        if (!(key in dictu)) {
          dictu[key] = 1;
        } else {
          dictu[key] += 1;
        }
      }
    }
  }
  console.log(dictu);
});
