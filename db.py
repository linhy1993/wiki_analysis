# cell 1
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

MUSEUM_DATABASE_URI = 'sqlite:///museum.sqlite'  # db path
CITY_DATABASE_URI = 'sqlite:///city_info.sqlite'  # db path

Base = declarative_base()


# cell 2
class Museum(Base):  # model
    __tablename__ = 'museum'

    id = Column(Integer, primary_key=True)
    Museum_Name = Column(String(50))
    City = Column(String(50))
    Country = Column(String(50))
    Number_Of_Visitors = Column(Integer)
    Year_Reported = Column(String(10))
    Population_Of_City = Column(Integer)


class City(Base):  # model
    __tablename__ = 'city_info'

    index = Column(Integer, primary_key=True)
    city = Column(String(50))
    country = Column(String(50))
    lat = Column(String(50))
    lng = Column(String(50))
    population = Column(Integer)


# cell 3
class Database(object):  # db init and operation
    def __init__(self, db_uri):
        self.engine = None
        self.session = None
        self.db_uri = db_uri
        self.create_engine()
        self.create_session()

    def create_engine(self):
        self.engine = create_engine(self.db_uri)

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine, checkfirst=True)

    def create_session(self):
        self.session = sessionmaker(bind=self.engine)()

    def close(self):
        self.session.close()
