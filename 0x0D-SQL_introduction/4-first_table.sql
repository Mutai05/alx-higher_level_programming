-- 4-first_table.sql
-- Task: Create a table named first_table in the current database

-- Create the first_table if it does not exist
CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
