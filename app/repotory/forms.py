from dataclasses import dataclass

from app.repotory.basemodels import Base


@dataclass
class Form(Base):
    id: int
    type: str = None

    def get_all(self):
        all_ids = self.engine.execute(f"SELECT id FROM {self.tablename}").fetchall()
        return all_ids

    def get(self):
        list_columns = self.engine.execute(f"SELECT * FROM {self.tablename} WHERE id={self.id}").fetchall()
        if list_columns:
            self.id, self.type = list_columns[0]
        return self.__dict__

    def save(self):
        self.engine.execute(f"INSERT INTO {self.tablename} (type) VALUES ('{self.type}')")

    def update(self):
        self.engine.execute(f"UPDATE {self.tablename} SET type='{self.type}' WHERE id={self.id}")

    def delete(self):
        self.engine.execute(f"DELETE FROM {self.tablename} WHERE id={self.id}")

    def clear(self):
        self.engine.execute(f"DELETE FROM {self.tablename}")
