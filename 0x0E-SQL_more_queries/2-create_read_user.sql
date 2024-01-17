-- Create the database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant usage on all databases to user_0d_2
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grant SELECT privilege only on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Reload privileges to apply the changes
FLUSH PRIVILEGES;
