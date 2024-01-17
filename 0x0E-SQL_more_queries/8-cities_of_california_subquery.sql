-- Use the hbtn_0d_usa database
-- Select all cities of California without using JOIN

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
