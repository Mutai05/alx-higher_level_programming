-- 5-full_table.sql
-- Task: Print the full description of the table first_table from the specified database

-- Use the information_schema database to get the table structure
SELECT
  table_name AS 'Table',
  table_definition AS 'Create Table'
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
