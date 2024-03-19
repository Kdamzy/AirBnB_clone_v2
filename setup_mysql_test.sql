-- Create a database hbnh_test_db
-- Create a new user hbnb_test with password hbnb_test_pwd
-- Give hbnb_test all privileges to the database hbnb_test_db
-- Give hbnb_test SELECT privilege on the database performance_schema
-- if the database hbnb_test_db or the user hbnb_test already exists, do nothing


CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
