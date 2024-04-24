#!/usr/bin/node
const { error } = require('console');
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, content) => {
	if (error) {
		console.error(error);
	}
	else {
		console.log(content);
	}
});
