import mysql.connector

cnx = mysql.connector.connect(user = 'root', password= 'learning', host = '127.0.0.1', database = 'employees')

cnx.close()