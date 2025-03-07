#!/usr/bin/python3
"""
A script that changes the name of a State object from the database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(
        State, City.state_id == State.id
    ).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
