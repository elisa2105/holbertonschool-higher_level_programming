#!/usr/bin/python3
"""
Get state by it's name with sqlalchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    userd = argv[1]
    passd = argv[2]
    db_name = argv[3]
    param = argv[4]
    connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connection.format(userd, passd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_made = sessionmaker(bind=engine)
    session = session_made()
    found = session.query(State).filter(State.name == param)
    if found.count():
        print(found[0].id)
    else:
        print("Not found")
    session.close()
