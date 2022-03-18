DROP DATABASE IF EXISTS timeClockManager;

CREATE DATABASE timeClockManager;

CREATE TABLE staff(
sID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
sName varchar(100) NOT NULL,
sUserName varchar(100) NOT NULL,
sPassword varchar(100) NOT NULL
);

CREATE TABLE clock(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
sID INT,
clockIn DATETIME,
clockOut DATETIME,
FOREIGN KEY (sID) REFERENCES staff(sID)
);
