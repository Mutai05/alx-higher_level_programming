-- 8-count_89.sql
-- Task: Display the number of records with id = 89 in the table first_table

-- Use the specified database
USE hbtn_0c_0;

-- Count the number of records with id = 89
SELECT COUNT(*) FROM first_table WHERE id = 89;
