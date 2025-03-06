#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__== "__main__":
    # Connect to the MySQL database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states, ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results and print them
    for state in cur.fetchall():
        print(state)

    # Close the cursor and database connection
    cur.close()
    db.close()
