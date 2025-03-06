#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states.
Safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cur.execute(query, (state_name,))

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
