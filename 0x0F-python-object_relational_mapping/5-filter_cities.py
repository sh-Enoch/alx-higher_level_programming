#!/usr/bin/python3
"""Takes state name and list all cities."""

import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    passw = sys.argv[2]
    dbase = sys.argv[3]
    state_n = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, username=uname,
                         passwd=passw, db=dbase)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities\
                JOIN states ON cities.state_id=states.id\
                WHERE states.name LIKE BINARY %s ORDER BY\
                cities.id ASC", (sys.argv[4], ))
    data = cur.fetchall()
    print(", ".join([row[2] for row in data if row[r] == sys.argv[4]]))
