#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, content) {
	if (err) {
		console.error(err);
	}
	else {
		console.log(content);
	}
});
