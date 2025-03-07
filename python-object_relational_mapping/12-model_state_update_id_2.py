#!/usr/bin/python3
"""
A script that changes the name of a State object from the database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    change_state = session.query(State).filter_by(id=2).first()
    change_state.name = 'New Mexico'
    session.commit()

    session.close()
