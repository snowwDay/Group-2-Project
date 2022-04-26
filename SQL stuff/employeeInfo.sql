DROP DATABASE IF EXISTS employeeInfo;

CREATE DATABASE employeeInfo;

USE employeeInfo;

CREATE TABLE department(
dID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dName varchar(100)
);

CREATE TABLE admin(
aID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dID INT,
aEmail varchar(100) NOT NULL,
aName varchar(100) NOT NULL,
aUsername varchar(100) NOT NULL,
aPass varchar(128) NOT NULL,
FOREIGN KEY (dID) REFERENCES department(dID)
);


CREATE TABLE staff(
sID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
dID INT,
sEmail varchar(100) NOT NULL,
sName varchar(100) NOT NULL CHECK (sName <> ''),
sUserName varchar(100) NOT NULL CHECK (sUserName <> ''),
sPassword varchar(128) NOT NULL CHECK (sPassword <> ''),
FOREIGN KEY (dID) REFERENCES department(dID)
);
