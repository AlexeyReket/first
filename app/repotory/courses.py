from dataclasses import dataclass

from app.repotory.basemodels import Base


@dataclass
class Course(Base):
    id: int
    num: int = None

    def get(self):
        list_columns = self.engine.execute(f"SELECT * FROM {self.tablename} WHERE id={self.id}").fetchall()
        self.id, self.num = list_columns[0]
        return self

    def save(self):
        self.engine.execute(f"INSERT INTO {self.tablename} (id,num) VALUES ({self.id}, {self.num})")

    def update(self):
        self.engine.execute(f"UPDATE {self.tablename} SET num=%s WHERE id={self.id}")

    def delete(self):
        self.engine.execute(f"DELETE FROM {self.tablename} WHERE id={self.id}")
