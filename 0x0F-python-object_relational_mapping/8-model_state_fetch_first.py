#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base,  State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_connect = (f"mysql+mysqldb://{argv[1]}:{argv[2]}"
                  f"@localhost:3306/{argv[3]}")
    engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print(f'{state.id}: {state.name}')
    else:
        print("Nothing")
