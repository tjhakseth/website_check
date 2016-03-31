"""Database for Lookout"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

Base = declarative_base()

def db_connect():

    engine = create_engine('postgresql://localhost/lookoutdb')

    return engine

def create_status_table(engine):

    Base.metadata.create_all(engine)

class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, autoincrement=True, primary_key=True)
    HTTP_status_code = Column(String(3), nullable=False)
    url = Column(String(500), nullable=False)
    timestamp = Column(String(500), nullable=False)
