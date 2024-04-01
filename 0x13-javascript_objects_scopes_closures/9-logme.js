#!/usr/bin/node
let existing = 0;

exports.logMe = function (item) {
	console.log(existing +  ': ' + item);
	existing++;
};
