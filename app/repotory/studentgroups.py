from dataclasses import dataclass

from app.repotory.basemodels import Base
from app.repotory.courses import Course
from app.repotory.facultys import Faculty
from app.repotory.forms import Form


@dataclass
class StudentGroup(Base):
    id: int
    name: str = None
    faculty: Faculty = None
    course: Course = None
    form: Form = None

    def get(self):
        list_columns = self.engine.execute(f"SELECT * FROM {self.tablename} WHERE id={self.id}").fetchall()
        self.id, self.name, self.faculty, self.course, self.form = list_columns[0]
        return self

    def save(self):
        self.engine.execute(
            f"INSERT INTO {self.tablename} (name,faculty,course,form) VALUES ({self.name},{self.faculty},{self.course},{self.form}) WHERE id={self.id}")

    def update(self):
        self.engine.execute(
            f"UPDATE {self.tablename} SET name={self.name},faculty={self.faculty},course={self.course},form={self.form} WHERE id={self.id}")

    def delete(self):
        self.engine.execute(f"DELETE FROM {self.tablename} WHERE id={self.id}")
