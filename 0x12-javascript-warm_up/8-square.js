#!/usr/bin/node

if (process.argv[2] == undefined || isNaN(process.argv[2])) {
	console.log('Missing size');
}
else {
	const size = parseInt(process.argv[2]);
	for (let i = 1; i <= size; i++) {
		console.log('x'.repeat(size));
	}
}
