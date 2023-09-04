import mysql.connector

connection = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="sakila"
)

cur = connection.cursor()
cur.execute("SELECT * FROM customer")
result = cur.fetchall()

for row1 in result:
	print(row1)