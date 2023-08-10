import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

curs = database.cursor()

curs.execute("create database crm ")

print("all done")