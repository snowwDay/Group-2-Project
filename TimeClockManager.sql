DROP DATABASE IF EXISTS timeClockManager;

CREATE DATABASE timeClockManager;

CREATE TABLE staff(
sID INT PRIMARY KEY AUTO_INCREMENT,
sName varchar(100) NOT NULL CHECK (sName <> ''),
sUserName varchar(100) NOT NULL CHECK (sUserName <> ''),
sPassword varchar(100) NOT NULL CHECK (sPassword <> '')
);

CREATE TABLE clock(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
clockIn DATETIME,
clockOut DATETIME,
status enum('In','Out') NOT NULL,
FOREIGN KEY (sID) REFERENCES staff(sID)
);

CREATE TABLE salts(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
salt varchar(15) NOT NULL CHECK (salt <> ''),
FOREIGN KEY (sID) REFERENCES staff(sID)
);

