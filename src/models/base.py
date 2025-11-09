from sqlalchemy.ext.declarative import declarative_base
from database import Base

class BaseModel:
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}