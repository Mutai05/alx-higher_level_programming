#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from MySQL injection).
"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    db_cursor = db_connect.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    db_cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows_selected = db_cursor.fetchall()

    # Display results
    for row in rows_selected:
        print(row)

    # Close cursor and database connection
    db_cursor.close()
    db_connect.close()
