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

SELECT * FROM timeClockManager.staff;

Insert into timeClockManager.staff(sName, sUserName, sPassword)
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

SELECT * FROM timeClockManager.clock;

Insert into timeClockManager.clock(clockIN, clockOut)
values('','');

UPDATE clock
set clockIN = ''
where clockIN = '';

UPDATE clock
set clockOut = ''
where clockOut = '';

Delete from timeClock.Manager.clock
where sID = '';
-- testing
