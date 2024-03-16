#!/usr/bin/python3
"""
Takes the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the database
    dbconnect = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    dbcursor = dbconnect.cursor()

    # Execute the query to select cities with their corresponding state names
    dbcursor.execute("""
                     SELECT
                        cities.id, cities.name
                     FROM
                        cities
                     JOIN
                        states
                     ON
                        cities.state_id = states.id
                     WHERE
                        states.name LIKE BINARY %(state_name)s
                     ORDER BY
                        cities.id ASC

                     """, {'state_name': argv[4]})

    # Fetch all rows
    rows = dbcursor.fetchall()

    # Display each row in the specified format
    print(", ".join([row[1] for row in rows]))

    # Close cursor and database connection
    dbcursor.close()
    dbconnect.close()
