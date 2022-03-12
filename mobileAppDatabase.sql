CREATE DATABASE IF NOT EXISTS mobileApp ; 


CREATE TABLE users (
userID int(50) NOT NULL auto_increment, 
email varchar(200) NOT NULL,
pass varchar(200) NOT NULL,  # will change later. need encyption
firstName varchar(200) NOT NULL,
lastName varchar(200) NOT NULL,
major varchar(100) NOT NULL, #have to make a list of majors
gender varchar(50),
profilePic varchar(200),
PRIMARY KEY (userID),
UNIQUE KEY email (email)
);

CREATE TABLE message(
messageID int(50) NOT NULL auto_increment, 
senderID int(50) NOT NULL,
recieverID int(50) NOT NULL,
content text NOT NULL,
PRIMARY KEY (messageID),
FOREIGN KEY (senderID) REFERENCES users(userID),
FOREIGN KEY (recieverID) REFERENCES users(userID)

);

CREATE TABLE tutors(
tutorID int(50) NOT NULL auto_increment,
userID int(50) NOT NULL,
phoneNumber int(10),
price decimal(4,2),
PRIMARY KEY (tutorID),
FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE studyGroup(
studyID int(50) NOT NULL,
memberID int(50) NOT NULL,
size int(10) NOT NULL,
topic varchar(50) NOT NULL,
meetingDate date NOT NULL,
meetingTime time NOT NULL,
PRIMARY KEY (studyID),
FOREIGN KEY (memberID) REFERENCES users(userID)
);





# Queries #
