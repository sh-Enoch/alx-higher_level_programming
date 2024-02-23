#!/usr/bin/python3
"""Prints the first state objects from dabse."""
import sys
from sqlalchemy.orm import sessionmker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(usr, pw, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(state.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}". format(stae.id, stae.name))
