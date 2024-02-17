-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
--Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
use hbtn_0d_usa;
--create a table
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
	FOREIGN KEY (state_id) REFERENCES id(state)
);
