#!/usr/bin/node
const a = process.argv.length;
console.log(a === 2 ? 'No argument' : a === 3 ? 'Argument found' : 'Argument found');
