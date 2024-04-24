#!/usr/bin/node

// Import the 'fs' module to work with the file system
const fs = require('fs');

// Write the specified string to the specified file
// The file path is provided as the third command-line argument (process.argv[2])
// The string to write is provided as the fourth command-line argument (process.argv[3])
// The 'utf8' parameter specifies the encoding of the string (UTF-8)
fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
    // Check if an error occurred during the writing process
    if (error) {
        // If an error occurred, log the error to the console
        console.error(error);
    }
});
