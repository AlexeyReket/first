from sqlalchemy import create_engine  # Table, Integer, Column, String, MetaData, ForeignKey
# from sqlalchemy.orm import mapper
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

engine = create_engine("sqlite:///docs.db")
# Base = declarative_base()
file = open("migrations/1.sql", "r")
sqlText = file.read().split(sep=";\n")
file.close()
for line in sqlText:
    engine.execute(text(line))
