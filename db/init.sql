CREATE DATABASE proj_db;

use proj_db;

CREATE TABLE users (userID INT AUTO_INCREMENT PRIMARY KEY, userName VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL);