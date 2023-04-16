#!/usr/bin/python3

""" A script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE \
                    BINARY 'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()

    count = 0
    while (count < len(states)):
        print("{}".format(states[count]))
        count += 1
