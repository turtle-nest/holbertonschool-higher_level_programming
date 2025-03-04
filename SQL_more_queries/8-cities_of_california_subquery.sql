-- Cities of California
-- A script that lists all the cities of California that can be found in the database

-- List all the cities
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
