#!/usr/bin/python3
''' adds object Louisiana to the database '''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    dbConnector = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(dbConnector.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    addState = State("Louisiana")
    session.add(addState)
    session.commit()

    query = session.query(State).filter(
        State.name == 'Louisiana')

    if query.count() > 0:
        for instance in query:
            print(str(instance.id))

    session.close()
