#!/usr/bin/node
let arr;
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  arr = process.argv.slice(2);
  arr.sort(function (a, b) { return a - b; });
  arr.reverse();
  console.log(arr[1]);
}
