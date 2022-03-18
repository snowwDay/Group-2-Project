DROP DATABASE IF EXISTS timeClockManager;

CREATE DATABASE timeClockManager;

CREATE TABLE staff(
sID INT PRIMARY KEY AUTO_INCREMENT,
sName varchar(100),
sUserName varchar(100),
sPassword varchar(100)
);

CREATE TABLE clock(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
clockIn DATETIME,
clockOut DATETIME,
FOREIGN KEY (sID) REFERENCES staff(sID)
);
