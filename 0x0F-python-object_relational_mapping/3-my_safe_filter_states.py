#!/usr/bin/python3
"""This script takes arguments and displays values in the states table."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(port=3306, host='localhost', user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()

    query = ('SELECT * FROM states WHERE name = ? ORDER BY id ASC')
    cursor.execute(query, (state_name,))

    all_states = cursor.fetchall()
    for row in all_states:
        print(row)
    cursor.close()
    db.close()
