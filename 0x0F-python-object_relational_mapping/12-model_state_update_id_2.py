#!/usr/bin/python3
"""
Updating name sqlalchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    userd = argv[1]
    passd = argv[2]
    db_name = argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connection.format(userd, passd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_made = sessionmaker(bind=engine)
    session = session_made()
    session.query(State).filter_by(id=2).update({"name": "New Mexico"})
    session.commit()
    session.close()
