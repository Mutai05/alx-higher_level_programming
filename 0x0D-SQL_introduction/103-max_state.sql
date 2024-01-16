-- 103-max_state.sql
-- Task: Display the max temperature of each state ordered by State name

-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Display the max temperature of each state ordered by State name
SELECT state, MAX(temperature) AS 'max_temp'
FROM temperature_data
GROUP BY state
ORDER BY state;
