DROP DATABASE IF EXISTS timeClockManager;

CREATE DATABASE timeClockManager;

USE timeClockManager;

CREATE TABLE department(
dID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
aID INT NOT NULL,
dName varchar(100),
);

CREATE TABLE admin(
aID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dID INT,
aName varchar(100) NOT NULL,
FOREIGN KEY (dID) REFERENCES department(dID)
);


CREATE TABLE staff(
sID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dID INT,
admin INT NOT NULL,
sName varchar(100) NOT NULL CHECK (sName <> ''),
FOREIGN KEY (dID) REFERENCES department(dID)
);

CREATE TABLE clock(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
clockIn DATETIME NOT NULL default current_timestamp,
clockOut DATETIME NOT NULL default current_timestamp,
status enum('In','Out','Break') NOT NULL,
FOREIGN KEY (sID) REFERENCES staff(sID)
);

CREATE TABLE schedule(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
sID INT,
workDate DATE NOT NULL,
startTime TIME NOT NULL,
endTime TIME NOT NULL,
timeOff BOOLEAN, # (on break) 0 for no, 1 for yes
FOREIGN KEY (sID) REFERENCES staff(sID)
);

CREATE TABLE staff_salts(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
salt char(32) NOT NULL CHECK (salt <> ''),
FOREIGN KEY (sID) REFERENCES staff(sID)
);

CREATE TABLE admin_salts(
id INT PRIMARY KEY AUTO_INCREMENT,
aID INT,
salt char(32) NOT NULL CHECK (salt <> ''),
FOREIGN KEY (aID) REFERENCES admin(aID)
);

CREATE TABLE tokens(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT NOT NULL,
ranks INT NOT NULL,
creationDate DATETIME NOT NULL default current_timestamp,
token char(32) NOT NULL CHECK (token <> ''),
FOREIGN KEY (sID) REFERENCES staff(sID)
);
