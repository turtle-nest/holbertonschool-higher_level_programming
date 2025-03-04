-- Full creation
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
