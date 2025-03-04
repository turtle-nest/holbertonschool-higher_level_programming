-- Full creation
-- a script that creates a table called second_table in the database hbtn_0c_0 and adds multiple rows

-- Use the database hbtn_0c_0
USE hbtn_0c_0;

-- Create the table second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- Insert multiple rows into the table second_table
INSERT INTO second_table (id, name, score)
VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'Georges', 8);
ON DUPLICATE KEY UPDATE
	id = VALUES(id), name = VALUES(name), score = VALUES(score);
