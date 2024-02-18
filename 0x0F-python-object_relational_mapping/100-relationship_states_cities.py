#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # MySQL connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creating the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name), pool_pre_ping=True)

    # Creating the tables
    Base.metadata.create_all(engine)

    # Creating a session
    session = Session(engine)

    # Adding California and San Francisco to the database
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    new_state.cities.append(new_city)

    # Committing the changes
    session.add(new_state)
    session.commit()

    # Closing the session
    session.close()
