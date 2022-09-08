-- creates the database hbtn_0d_2 and the user user_0d_2.
-- creating database hbtn0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
-- granting SELECT privileges for user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
