#!/usr/bin/node
const toparse = process.argv[2];
const parsedNum = parseInt(toparse);
if (isNaN(parsedNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedNum}`);
}
