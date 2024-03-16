#!/usr/bin/python3
"""
list all  states name starting with 'N' from `hbtn_0e_0_usa
database
"""
import MySQLdb
from sys import argv

"""
access the database
"""

if __name__ == '__main__':
    dbconnect = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    dbcursor = dbconnect.cursor()
    dbcursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC"
    )
    rows = dbcursor.fetchall()
    for row in rows:
        print(row)
    dbcursor.close()
    dbconnect.close()
