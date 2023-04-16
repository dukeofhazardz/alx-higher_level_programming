#!/usr/bin/python3

""" A script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT c.id, c.name, s.name FROM states AS s INNER JOIN \
                    cities AS c ON c.state_id=s.id ORDER BY c.id ASC")
    states = cursor.fetchall()

    count = 0
    while (count < len(states)):
        print("{}".format(states[count]))
        count += 1
