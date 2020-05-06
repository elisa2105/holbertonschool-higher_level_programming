#!/usr/bin/node
const lenA = process.argv.length;
if (lenA === 2) {
  console.log('No argument');
} else if (lenA === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
