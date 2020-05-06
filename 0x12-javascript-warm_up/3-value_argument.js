#!/usr/bin/node
let lenA = 0;
process.argv.forEach((element) => { lenA++; });
if (lenA === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
