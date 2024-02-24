#!/usr/bin/python3
"""Script to print all state with a letter a database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_stae import State

if __name__ == "__main__":
    engine = create_engine("mwsql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
