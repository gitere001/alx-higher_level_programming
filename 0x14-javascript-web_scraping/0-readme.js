#!/usr/bin/node

// Import the 'fs' module to work with the file system
const fs = require('fs');

// Read the file specified as a command-line argument
fs.readFile(process.argv[2], 'utf8', function (err, content) {
    // Check if an error occurred during file reading
    if (err) {
        // If an error occurred, log the error to the console
        console.error('Error reading the file:', err);
    } else {
        // If no error occurred, log the file content to the console
        console.log(content);
    }
});
