from dataclasses import dataclass

from app.repotory.basemodels import Base
from app.repotory.courses import Course
from app.repotory.facultys import Faculty
from app.repotory.forms import Form


@dataclass
class StudentGroup(Base):
    id: int
    name: str = None
    faculty_id: int = None
    course_id: int = None
    form_id: int = None

    @property
    def faculty(self):
        return Faculty(self.faculty_id).get()

    @property
    def course(self):
        return Course(self.course_id).get()

    @property
    def form(self):
        return Form(self.form_id).get()

    def get_all(self):
        all_ids = self.engine.execute(f"SELECT id FROM {self.tablename}").fetchall()
        return all_ids

    def get(self):
        list_columns = self.engine.execute(f"SELECT * FROM {self.tablename} "
                                           f"INNER JOIN Faculty ON faculty_id = Faculty.id "
                                           f"INNER JOIN Course ON course_id = Course.id "
                                           f"INNER JOIN Form ON form_id = Form.id "
                                           f"WHERE {self.tablename}.id = {self.id} ").fetchall()
        if list_columns:
            self.id, self.name, self.faculty_id, self.course_id, self.form_id, self.faculty_id, self.facluty_name , self.course_id, self.course_num, self.form_id, self.form_type = list_columns[0]
        return self.__dict__

    def save(self):
        self.engine.execute(
            f"INSERT INTO {self.tablename} (name,faculty_id,course_id,form_id) VALUES ('{self.name}',{self.faculty_id},{self.course_id},{self.form_id})")

    def update(self):
        self.engine.execute(
            f"UPDATE {self.tablename} SET name='{self.name}',faculty_id={self.faculty_id},course_id={self.course_id},form_id={self.form_id} WHERE id={self.id}")

    def delete(self):
        self.engine.execute(f"DELETE FROM {self.tablename} WHERE id={self.id}")

    def clear(self):
        self.engine.execute(f"DELETE FROM {self.tablename}")
