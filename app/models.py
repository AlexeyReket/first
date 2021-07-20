from gino import Gino
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = Gino()


class GroupUsers(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    def __repr__(self):
        return "<Group('%s')>" % self.name


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # group = Column(ForeignKey(Group))

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name, self.fullname, self.nickname)