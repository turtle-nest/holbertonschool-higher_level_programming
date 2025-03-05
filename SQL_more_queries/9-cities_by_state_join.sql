-- Cities by States
-- a script that lists all cities contained in the database

-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- List all cities by states
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
