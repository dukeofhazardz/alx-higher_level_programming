#!/usr/bin/python3

""" A script that prints the first State object from
    the database hbtn_0e_6_usa """

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if (first_state):
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
