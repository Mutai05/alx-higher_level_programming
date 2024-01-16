-- 12-no_cheating.sql
-- Task: Update the score of Bob to 10 in the table second_table, without using Bob's id value

-- Use the specified database
USE hbtn_0c_0;

-- Update the score of Bob to 10 in second_table
UPDATE second_table SET score = 10 WHERE name = 'Bob';
