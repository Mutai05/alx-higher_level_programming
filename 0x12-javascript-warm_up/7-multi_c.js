#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x) || parseInt(x) <= 0) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < x; i++) {
        console.log('C is fun');
    }
}

