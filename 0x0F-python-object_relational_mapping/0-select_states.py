#!/usr/bin/python3
"""
list  all states from the hbtn_Oe_0_usa database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """accessing database and get states"""
    dbconnect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )
    cursor = dbconnect.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)  # Print each row
    cursor.close()  # Close the cursor
    dbconnect.close()  # Close the database connection
