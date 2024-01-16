-- 11-best_score.sql
-- Task: List records with a score >= 10 in the table second_table, ordered by score, in the specified database

-- Use the specified database
USE hbtn_0c_0;

-- Select records with score >= 10 from second_table and order by score (top score first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
