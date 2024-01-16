-- 16-no_link.sql
-- Task: List all records of the table second_table with a valid name, ordered by descending score

-- Use the specified database
USE hbtn_0c_0;

-- List all records with a valid name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
