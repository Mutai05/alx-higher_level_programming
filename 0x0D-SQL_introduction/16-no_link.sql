-- 16-no_link.sql
-- Task: List all records of the table second_table with a valid name, ordered by descending score
-- Use the specified database
-- List all records with a valid name, ordered by descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
