#!/usr/bin/python3
"""Script that prints all cities from the database."""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, username=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()
    query = ("SELECT cities.id states.name cities.name FROM states cities WHERE
             cities.state_id=state.id ORDER BY cities.id ASC")
    cursor.execute(query)

    all_cities = cursor.fetchall()
    for row in all_cities:
        print(row)
    cursor.close()
    db.close()
