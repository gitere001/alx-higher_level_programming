#!/usr/bin/python3
"""
list all the states in hbtn_0e_6_usa database

"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    accessing  data from the database
    """
    db_connect = (f"mysql+mysqldb://{argv[1]}:{argv[2]}"
                  f"@localhost:3306/{argv[3]}")

    engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(State).order_by(State.id):
        print(f'{inst.id}: {inst.name}')
