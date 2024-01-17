-- Use the hbtn_0d_usa database
-- Select all cities and their corresponding states using JOIN

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

