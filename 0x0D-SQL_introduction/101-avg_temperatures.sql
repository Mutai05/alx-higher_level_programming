-- 101-avg_temperatures.sql
-- Task: Display the average temperature (Fahrenheit) by city ordered by temperature (descending)

-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Display the average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS 'avg_temp'
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
