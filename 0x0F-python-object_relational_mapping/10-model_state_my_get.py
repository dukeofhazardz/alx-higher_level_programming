#!/usr/bin/python3

""" A script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa """

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    s_name = sys.argv[4]
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    _state = session.query(State).filter(State.name == s_name).first()
    try:
        print(_state.id)
    except Exception:
        print("Not found")
