import mysql.connector

connection = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="bdescola"
)

cursor = connection.cursor()
sql="INSERT INTO aluno (nome,endereco,telefone) VALUES (%s, %s, %s)"
data = (
    'Micael Cadete',
    'Av teste, 156',
    '911234542'
)
cursor.execute(sql, data)
connection.commit()
userid = cursor.lastrowid
cursor.close()
connection.close
print("Foi cadastrado o novo usuário de ID: ", userid)
