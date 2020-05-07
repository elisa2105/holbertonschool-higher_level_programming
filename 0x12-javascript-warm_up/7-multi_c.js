#!/usr/bin/node
let i = process.argv[2];
i = parseInt(i);
if (isNaN(i)) {
  console.log('Missing number of occurences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
