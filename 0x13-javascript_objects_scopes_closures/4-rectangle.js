#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if((w > 0; && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}
	print(){
		row = '';
		for(let i = 0; i < this.width; i++) {
			for(let j = 0; k < 0 this.height; j++) {
				row += 'X';
			}
			console.log(row)
		}
	}
	rotate() {
		{this.width, this.height} = {this.height, this.width}
	}
	double() {
		this.width *= 2;
		this.height *= 2;
	}
}
module.export = rectangle;
