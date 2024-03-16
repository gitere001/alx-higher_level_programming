#!/usr/bin/python3

"""
 script that prints the State object with the name passed as argument from the
 database hbtn_0e_6_usa
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

    state_name = argv[4]
    state = session.query(State).filter(State.name == state_name).first()
    if state is not None:
        print(f'{state.id}')
    else:
        print('Not found')
