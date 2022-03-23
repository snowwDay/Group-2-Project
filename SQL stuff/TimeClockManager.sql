DROP DATABASE IF EXISTS timeClockManager;

CREATE DATABASE timeClockManager;


CREATE TABLE department(
dID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dName varchar(100)
);

CREATE TABLE admin(
aID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dID INT,
aName varchar(100) NOT NULL,
aUsername varchar(100) NOT NULL,
aPass varchar(100) NOT NULL,
FOREIGN KEY (dID) REFERENCES department(dID)
);


CREATE TABLE staff(
sID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dID INT,
sName varchar(100) NOT NULL CHECK (sName <> ''),
sUserName varchar(100) NOT NULL CHECK (sUserName <> ''),
sPassword varchar(100) NOT NULL CHECK (sPassword <> ''),
FOREIGN KEY (dID) REFERENCES department(dID)
);

CREATE TABLE clock(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
clockIn DATETIME,
clockOut DATETIME,
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

CREATE TABLE scheduleList(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
sID INT,
status enum('In','Out'),
FOREIGN KEY (sID) REFERENCES staff(sID),
FOREIGN KEY (status) REFERENCES clock(status) 
);

CREATE TABLE unscheduledList(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
sID INT,
FOREIGN KEY (sID) REFERENCES staff(sID)
);


CREATE TABLE salts(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
salt varchar(15) NOT NULL CHECK (salt <> ''),
FOREIGN KEY (sID) REFERENCES staff(sID)
);
