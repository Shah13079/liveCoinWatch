import string
from typing import Text
from sqlalchemy import INTEGER, create_engine, Column, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String,  Float,BigInteger )
from sqlalchemy.dialects.mysql import VARCHAR, TEXT
from scrapy.utils.project import get_project_settings
from sqlalchemy.dialects import mysql


DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class LiveCoin_data_model(DeclarativeBase):
    __tablename__ = "live_coin_watch_table"

    
    code= Column('code',String(250),primary_key=True)
    name = Column('name', String(250))
    color = Column('color', String(250))
    rank = Column('rank', Integer)
    price = Column('price', String(250))
    cap = Column('cap', String(250))
    totalCap = Column('totalCap', String(250))
    maxSupply = Column('maxSupply', String(250) )
    totalSupply = Column('totalSupply',String(250))
    circulating = Column('circulating', String(250))
    issued = Column('issued', String(250))
    volmcap = Column('volmcap', String(250))
    exchanges = Column('exchanges', INTEGER())
    elisted = Column('elisted', TEXT())
    twitter = Column('twitter', String(250))
    reddit = Column('reddit', String(250))
    telegram = Column('telegram', String(250))
    delta = Column('delta', TEXT())
    deltav = Column('deltav', TEXT())



