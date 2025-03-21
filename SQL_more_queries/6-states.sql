-- States table
-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)

-- Create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table states
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT NOT NULL UNIQUE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
