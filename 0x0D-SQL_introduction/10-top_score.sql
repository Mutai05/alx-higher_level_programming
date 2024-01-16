-- 10-top_score.sql
-- Task: List all records of the table second_table, ordered by score, in the specified database

-- Use the specified database
USE hbtn_0c_0;

-- Select records from second_table and order by score (top score first)
SELECT score, name FROM second_table ORDER BY score DESC;
