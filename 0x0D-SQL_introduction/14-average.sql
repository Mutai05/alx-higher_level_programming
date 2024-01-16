-- 14-average.sql
-- Task: Compute the average score of all records in the table second_table

-- Use the specified database
USE hbtn_0c_0;

-- Compute the average score from second_table
SELECT AVG(score) AS 'average' FROM second_table;
