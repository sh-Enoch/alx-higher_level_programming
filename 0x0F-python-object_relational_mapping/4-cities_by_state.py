#!/usr/bin/python3
"""cript that lists all states with a name starting with N."""


import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    st = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    new = ('SELECT cities.id, cities.name, states.name
            FROM cities JOIN states WHERE cities.state_id=states.id
	    ORDER BY id ASC')
           .format(st))
    cur.execute(new)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
