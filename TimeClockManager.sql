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
clockIn DATETIME NOT NULL CHECK (clockIn <> ''),
clockOut DATETIME NOT NULL CHECK (clockOut <> ''),
FOREIGN KEY (sID) REFERENCES staff(sID)
);

CREATE TABLE salts(
id INT PRIMARY KEY AUTO_INCREMENT,
sID INT,
salt varchar(15) NOT NULL CHECK (salt <> ''),
FOREIGN KEY (sID) REFERENCES staff(sID)
);

SELECT * FROM staff;

Insert into staff(sName, sUserName, sPassword)
values('','','');

UPDATE staff
set sName = ''
where sname = '';

UPDATE staff
set sUsername = ''
where sUsername = '';

UPDATE staff
set sPassword = ''
where sPassword = '';

Delete from staff
where sID = '';

SELECT * FROM clock;

Insert into clock(clockIN, clockOut)
values('2019-01-01 12:00','2019-01-01 12:00');

UPDATE clock
set clockIN = '2019-01-01 12:00'
where clockIN = '2019-01-01 12:00';

UPDATE clock
set clockOut = '2019-01-01 12:00'
where clockOut = '2019-01-01 12:00';

Delete from clock
where sID = '';

