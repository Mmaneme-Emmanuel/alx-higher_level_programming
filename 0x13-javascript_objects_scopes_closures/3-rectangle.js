#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        let row = '';
        for (let i = 0; i < this.width; i++) {
            for (let j = 0; j < this.height; j++) {
                row += 'X';
            }
            console.log(row);
        }
    }
}
module.exports = Rectangle;
