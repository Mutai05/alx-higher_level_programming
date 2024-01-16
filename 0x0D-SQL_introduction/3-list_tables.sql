-- 3-list_tables.sql
-- Task: List all tables of a specified database

-- Use the information_schema database to get the list of tables in the specified database
SELECT table_name AS Tables_in_database
FROM information_schema.tables
WHERE table_schema = DATABASE();
