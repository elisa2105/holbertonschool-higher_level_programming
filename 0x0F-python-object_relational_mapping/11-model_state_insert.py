#!/usr/bin/python3
"""
Adding a state to a database using sqlalchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connection.format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_made = sessionmaker(bind=engine)
    session = session_made()
    insert_state = State(name="Louisiana")
    insert = session.add(insert_state)
    session.commit()
    print(session.query(State).filter(State.name == "Louisiana")[0].id)
    session.close()
