import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="",
  password="",
  database=""
)
cursor = db.cursor(buffered = True)
