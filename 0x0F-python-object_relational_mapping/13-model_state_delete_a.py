#!/usr/bin/python3

"""
 script that delete all states containing letter 'a' from the
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

    states_with_a = session.query(State).filter(State.name.contains('a')).all()

    if not states_with_a:
        print("no state containing 'a'")
    else:
        for state in states_with_a:
            session.delete(state)
        session.commit()
    session.close()
