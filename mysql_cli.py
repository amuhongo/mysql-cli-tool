import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='sua_base'
)

cursor = conn.cursor()
consulta = input("Digite sua consulta SQL: ")
cursor.execute(consulta)

for resultado in cursor:
    print(resultado)

conn.close()
