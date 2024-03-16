#!/usr/bin/python3
"""
takes an argument and display all values in state
where 'name' matches the argument
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
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC".format(argv[4]))
    rows = dbcursor.fetchall()
    for row in rows:
        print(row)
    dbcursor.close()
    dbconnect.close()
