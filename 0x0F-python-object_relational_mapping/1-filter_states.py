#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Validate the number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SELECT query for states starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
