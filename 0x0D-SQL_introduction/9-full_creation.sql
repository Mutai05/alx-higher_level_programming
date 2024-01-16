-- 9-full_creation.sql
-- Task: Create a table named second_table and add multiple rows in the specified database

-- Use the specified database
USE hbtn_0c_0;

-- Create the second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

-- Insert multiple rows into second_table
INSERT INTO second_table (id, name, score) VALUES
  (1, 'John', 10),
  (2, 'Alex', 3),
  (3, 'Bob', 14),
  (4, 'George', 8);
