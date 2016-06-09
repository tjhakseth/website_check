"""Database for sitecheck"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def db_connect(database):
    """Connects to database"""

    engine = create_engine(database)

    return engine


def create_status_table(engine):
    """Create tables in the database"""

    Base.metadata.create_all(engine)


class Status(Base):
    """Status Table"""

    __tablename__ = 'status'

    id = Column(Integer, autoincrement=True, primary_key=True)
    HTTP_status_code = Column(Integer, nullable=False)
    url = Column(String(500), nullable=False)
    timestamp = Column(DateTime, nullable=False)
