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



num = input("entry number")
text = input("entry:")
entry = ("INSERT INTO test (num, entry) VALUES ({}, '{}')".format(num,text))
cursor.execute(entry)

cnx.commit()
cursor.close()

cnx.close()