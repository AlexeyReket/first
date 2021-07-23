from dataclasses import dataclass

from app.repotory.basemodels import Base


@dataclass
class Faculty(Base):
    id: int
    name: str = None

    def get(self):
        list_columns = self.engine.execute(f"SELECT * FROM {self.tablename} WHERE id={self.id}").fetchall()
        self.id, self.name = list_columns[0]
        return self

    def save(self):
        self.engine.execute(f"INSERT INTO {self.tablename} (id,name) VALUES ({self.id},'{self.name}')")

    def update(self):
        self.engine.execute(f"UPDATE {self.tablename} SET name={self.name} WHERE id={self.id}")

    def delete(self):
        self.engine.execute(f"DELETE FROM {self.tablename} WHERE id={self.id}")
