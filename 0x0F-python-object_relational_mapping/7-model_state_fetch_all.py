#!/usr/bin/python3
"""
Listing all state SQLAlchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    userd = argv[1]
    passd = argv[2]
    db_name = argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(userd, passd, db_name),
                           pool_pre_ping=True)
    session_made = sessionmaker(bind=engine)
    session = session_made()
    query = session.query(State).order_by(State.id).all()
    for found in query:
        print('{}: {}'.format(found.id, found.name))
    session.close()
