#!/usr/bin/python3
"""
Takes an argument and displays all values in state where
'name' matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the database
    dbconnect = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    dbcursor = dbconnect.cursor()

    # Execute the query to select cities with their corresponding state names
    dbcursor.execute(
        "SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC"
    )

    # Fetch all rows
    rows = dbcursor.fetchall()

    # Display each row in the specified format
    for row in rows:
        print(row)

    # Close cursor and database connection
    dbcursor.close()
    dbconnect.close()
