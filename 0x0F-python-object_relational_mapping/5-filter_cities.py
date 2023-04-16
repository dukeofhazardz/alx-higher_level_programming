#!/usr/bin/python3

""" A script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute(f"SELECT c.name FROM cities AS c JOIN states AS s ON \
                    s.id=c.state_id WHERE s.name='{state_name}' \
                    ORDER BY c.id ASC")
    states = cursor.fetchall()

    '''count = 0
    while (count < len(states)):
        print("{}".format(states[count]))
        count += 1'''
    print(states)
