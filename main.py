import mysql.connector



config = {
  'user': 'root',
  'password': 'learning',
  'host': '127.0.0.1',
  'database': 'journal',
  'raise_on_warnings': True,
  'use_pure': False,
}


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

entry = ("INSERT INTO test (num, entry) VALUES (001, 'This is a test')")

cursor.execute(entry)

cnx.commit()
cursor.close()

cnx.close()