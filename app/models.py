from gino import Gino
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = Gino()


class User(Base):
    __tablename__ = "user"
    user_id = db.Column(db.Integer(), primary_key=True)
    nickName = Column(db.Unicode(), default="noname")


class TimeTable(Base):
    __tablename__ = "timetable"
    objName = Column(db.Unicode())
