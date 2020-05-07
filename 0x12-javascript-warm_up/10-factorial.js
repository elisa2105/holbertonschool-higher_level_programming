#!/usr/bin/node
const passedArg = process.argv[2];
const num = parseInt(passedArg);
const n = factorial(num);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else if (num < 0) {
    return 'does not exist';
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(n);
