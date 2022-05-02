import mysql.connector

sched_db = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="timeClockManager"
)
sched_cursor = sched_db.cursor(buffered = True)

emp_db = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="employeeInfo"
)
emp_cursor = emp_db.cursor(buffered = True)
