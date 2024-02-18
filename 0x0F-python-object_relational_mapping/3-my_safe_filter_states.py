#!/usr/bin/pyhton3
"""Escape SQL injection."""
import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pas = sys.argv[2]
    dbase = sys.argv[3]
    state_ = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, username=uname,
                         passwd=pas, database=dbase)
    cur = db.cursor()
    query = ("SELECT * FROM state WHERE name LIKE BINARY \'{}\'
             ORDER BY id ASC".format(state_))

    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
