from sqlalchemy import Column,Integer,String,DateTime,Text,Date
from datetime import datetime
from db import  *
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    username=Column(String(100),unique=True)
    email=Column(String(100),unique=True)
    password=Column(String(255))
    created_at = Column(DateTime, default=datetime.today())

class Subject(Base):
    __tablename__="sub"
    id=Column(Integer,primary_key=True)
    subject_name=Column(String(100),unique=True)
    exam_date=Column(Date)
    difficulty_lvl=Column(String(10))