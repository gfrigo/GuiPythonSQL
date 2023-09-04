import mysql.connector

connection = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="sakila"
)

n1=input('Qual nome deseja pesquisar? ')

cur = connection.cursor()
query="SELECT * FROM customer where first_name like '"+n1+"%'"
cur.execute(query)
result = cur.fetchall()

for row1 in result:
	print(row1)