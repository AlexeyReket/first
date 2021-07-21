import dataclasses
from abc import abstractmethod
from dataclasses import dataclass
from sqlalchemy import create_engine

engine = create_engine("sqlite:///docs.db")


class Base:
    @abstractmethod
    def get(self):
        """getting data from database by id"""
        """engine.execute("SELECT * FROM facultys WHERE id=%s" % self.id)"""

    @abstractmethod
    def save(self):
        """save object to database"""
        """engine.execute("INSERT INTO facultys (id,name) VALUES (%s,%s)" % (self.id, self.name))"""

    @abstractmethod
    def update(self):
        """update data in database by id"""
        """engine.execute("UPDATE facultys SET name=%s WHERE id=%s" % (self.name, self.id))"""


@dataclass()
class Faculty(Base):
    id: int
    name: str

    def get(self):
        engine.execute("SELECT * FROM facultys WHERE id=%s" % self.id)

    def save(self):
        engine.execute("INSERT INTO facultys (id,name) VALUES (%s,%s)" % (self.id, self.name))

    def update(self):
        engine.execute("UPDATE facultys SET name=%s WHERE id=%s" % (self.name, self.id))


@dataclass()
class Form(Base):
    id: int
    type: str

    def get(self):
        engine.execute("SELECT * FROM forms WHERE id=%s" % self.id)

    def save(self):
        engine.execute("INSERT INTO forms (id,type) VALUES (%s,%s)" % (self.id, self.type))

    def update(self):
        engine.execute("UPDATE forms SET type=%s WHERE id=%s" % (self.type, self.id))


@dataclass()
class Course(Base):
    id: int
    num: int

    def get(self):
        engine.execute("SELECT * FROM courses WHERE id=%s" % self.id)

    def save(self):
        engine.execute("INSERT INTO courses (id,num) VALUES (%s,%s)" % (self.id, self.num))

    def update(self):
        engine.execute("UPDATE courses SET num=%s WHERE id=%s" % (self.num, self.id))


@dataclass()
class StudentGroup(Base):
    id: int
    group_name: str
    faculty: Faculty
    course: Course
    form: Form

    def get(self):
        engine.execute("SELECT * FROM groups WHERE id=%s" % self.id)

    def save(self):
        engine.execute("INSERT INTO groups (id,name,faculty,course,form) VALUES (%s,%s,%s,%s,%s)" % (
            self.id, self.group_name, self.faculty, self.course, self.form))

    def update(self):
        engine.execute("UPDATE groups SET name=%s,faculty=%s,course=%s,form=%s WHERE id=%s" % (
            self.group_name, self.faculty, self.course, self.form, self.id))


@dataclass()
class TimeTable(Base):
    group_name: str = dataclasses.field()
    subjects: [str]
    timings: [str]
