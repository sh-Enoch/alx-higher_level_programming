#!/usr/bin/python3
"""Script lists all states from the database."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbase = sys.argv[3]

    db = MySQLdb.connect(port=3306, host="localhost", user=username,
                         passwd=password, database=dbase)
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
