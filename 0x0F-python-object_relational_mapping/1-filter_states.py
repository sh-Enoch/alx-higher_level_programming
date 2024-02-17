#!/usr/bin/python3
"""Lists all states where name is given."""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbase = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3307, username=username,
                         passwd=password, database=dbase)
    cur = db.cursor()
    query = ('SELECT * FROM states WHERE name LIKE BINARY "N%" 
             ORDER BY id ASC')
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
