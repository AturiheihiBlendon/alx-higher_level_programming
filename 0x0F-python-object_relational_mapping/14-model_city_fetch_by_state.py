#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

from model_city import City


if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    # cities = session.query(State, City).join(City).order_by(City.id).all()
    # for state, city in cities:
    #     print("{}: ({}) {}".format(state.name, city.id, city.name))

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
