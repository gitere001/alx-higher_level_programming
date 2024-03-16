#!/usr/bin/python3

"""
 script that changes the name of a State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_connect = (f"mysql+mysqldb://{argv[1]}:{argv[2]}"
                  f"@localhost:3306/{argv[3]}")
    engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)
    session = Session()

    the_state = session.query(State).filter(State.id == 2).first()

    if the_state:
        the_state.name = "New mexico"
        session.commit()
    else:
        print('State with id = 2 not found.')
