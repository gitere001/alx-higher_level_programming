#!/usr/bin/python3

"""
 Add the State object "Louisiana" to the database hbtn_0e_6_usa
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
