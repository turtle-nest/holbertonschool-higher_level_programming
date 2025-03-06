#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states.
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"\
        .format(state_name)
    cur.execute(query)

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
