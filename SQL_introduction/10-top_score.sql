-- List by best
-- a script that lists all records of the table second_table of the database

-- List all records of the table second_table ordered by score (top first)
SELECT score, name FROM second_table
ORDER BY score DESC, name;
