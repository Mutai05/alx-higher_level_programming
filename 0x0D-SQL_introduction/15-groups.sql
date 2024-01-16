-- 15-groups.sql
-- Task: List the number of records with the same score in the table second_table

-- Use the specified database
USE hbtn_0c_0;

-- List the number of records for each score, sorted by the number of records (descending)

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
