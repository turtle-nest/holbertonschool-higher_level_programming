-- Read user
-- a script that creates the database hbtn_0d_2 and the user user_0d_2

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database hbtn_0d2_
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
