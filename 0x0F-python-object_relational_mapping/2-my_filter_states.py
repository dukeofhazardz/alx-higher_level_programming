#!/usr/bin/python3

""" A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute(f"SELECT * FROM states WHERE name='{name}' \
                    ORDER BY states.id ASC")
    states = cursor.fetchall()

    count = 0
    while (count < len(states)):
        print("{}".format(states[count]))
        count += 1
