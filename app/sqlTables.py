from sqlalchemy import create_engine, Table, Integer, Column, String, MetaData
from sqlalchemy.orm import mapper


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name, self.fullname, self.password)


engine = create_engine("sqlite:///docs.db")
metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('fullname', String)
                    )
metadata.create_all(engine)
mapper(User, users_table)

user = User("Вася", "Василий", "hfsdjk2")
print(user)
print(user.id)
