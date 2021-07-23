from abc import abstractmethod, ABC

from sqlalchemy import create_engine


class Base(ABC):
    engine = create_engine("sqlite:///D:\\Projects\\Projects Pycharm\\first\\app\\docs.db")

    @property
    def tablename(self):
        if hasattr(self.__class__, "_tablename"):
            return self.__class__._tablename
        return self.__class__.__name__

    @abstractmethod
    def get(self):
        """get data from table by id"""

    @abstractmethod
    def save(self):
        """save data to table"""

    @abstractmethod
    def update(self):
        """update data in table"""
