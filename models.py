from sqlalchemy import Column, Integer, String
from database import Base

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    release_year = Column(String)
