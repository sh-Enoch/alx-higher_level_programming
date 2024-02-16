#!/usr/bin/python3
"""Script lists all states from the database."""
import MySQLdb
from sys import argv

def get_states(username, password, dbname):
    """List all states fom dbase."""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db = str(dbname))
    cur = bd.cursor()
    query = ("SELECT * FROM states ORDER BY id ASC;")
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

    if __name__ == '__main__':
        get_states(argv[1], argv[2], argv[3])
