#!/usr/bin/python3
"""Take in an argument and display its values."""
import MySQLdb
import argv from sys


if __name__ == "__main__":
    """Open a database  connection."""
    db =  MySQLdb.connect(host="localhost", port=3306, user= sys.argv[1],
                          db=sys.argv[3], passwd=sys[2)
    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}'
             ORDER BY id ASC").format(sys.argv[4])
    rows = cus=rsor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
