#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, database=hbtn_0e_0_usa)
 cur = db.cursor()
 query = ("SELECT * FROM states ORDER BY id ASC")
 cur.execute(query)
query_rows =  cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
