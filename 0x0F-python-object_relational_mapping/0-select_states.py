#!/usr/bin/python3
"""Script that lists all statesfrom dbase hbtn_0e_0_usa."""
import MySQLdb
from sys import argv


def get_states(username, password, dbname):
    """List all states from database."""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname))
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states(argv[1], argv[2], argv[3])
