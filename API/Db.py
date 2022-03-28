import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="timeClockManager"
)
cursor = db.cursor(buffered = True)
