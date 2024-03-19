-- Create a database hbnh_dev_db
-- Create a new user hbnb_dev with password hbnb_dev_pwd
-- Give hbnb_dev all privileges to the database hbnb_dev_db
-- Give hbnb_dev SELECT privilege on the database performance_schema
-- if the database hbnb_dev_db or the user hbnb_dev already exists, do nothing


CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
