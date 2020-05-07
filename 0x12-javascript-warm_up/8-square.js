#!/usr/bin/node
const square = 'X';
let size = process.argv[2];
size = parseInt(size);
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (let i = 0; i < size; i++) {
    console.log(square.repeat(size));
  }
}
