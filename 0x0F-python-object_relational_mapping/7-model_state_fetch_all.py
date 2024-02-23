#!/usr/bin/python3
"""list all states of dbase."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import state


if __name__ == "__main__":
    usrname = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(usrname, pw, db),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for sate in session.query(state).order_by(state.id):
        print("{}: {}".format(state.id, state.name))
