#!/usr/bin/python3
"""
a script that prints all City objects from the database hbtn_0e_14_usa

"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    db_connection = (f"mysql+mysqldb://{argv[1]}:{argv[2]}"
                     f"@localhost:3306/{argv[3]}")
    engine = create_engine(db_connection)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(State)
    for city, state in result.all():
        print(f"{state.name}: {city.id} {city.name}")

    session.close()
