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

insert into staff values (1,'User','user','pass');
insert into clock values (2,1,'2022-03-20 09:30',NULL,'In');
insert into schedule values (1,1,'2022-03-20','09:00','16:00',0);
select * from schedule;
delete from schedule where id = 1;

