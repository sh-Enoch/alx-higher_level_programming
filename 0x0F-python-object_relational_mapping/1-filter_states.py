#!/usr/bin/python3
"""Script that lists all statesfrom dbase hbtn_0e_0_usa."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY 'N%'
             ORDER BY id ASC")
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
