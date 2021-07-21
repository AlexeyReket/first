import dataclasses
import datetime

from gino import Gino
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = Gino()


@dataclass()
class Faculty:
    name: str


@dataclass()
class Form:
    type: str


@dataclass()
class Course:
    num: int


@dataclass()
class StudentGroup:
    group_name: str
    faculty_name: str = dataclasses.field()
    course_num: int = dataclasses.field()
    form_type: str = dataclasses.field()

    def __repr__(self):
        return "%s" % self.group_name


@dataclass()
class TimeTable:
    group_name: str = dataclasses.field()
    subjects: [str]
    timings: [str]


fac = Faculty("ФаМИ")
course = Course(1)
form = Form("Дневная")
group = StudentGroup("СДП-МАТ-201", fac, course, form)
timeTable = TimeTable(group, ["1", "2", "3"], ["10:05", "11:40", "13:30"])
print(timeTable)
