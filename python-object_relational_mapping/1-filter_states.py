#!/usr/bin/python3
"""
List all states with a name starting with N (upper N)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' \
                ORDER BY states.id ASC")

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
