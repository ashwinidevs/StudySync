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
    __tablename__="subjects"
    id=Column(Integer,primary_key=True)
    subject_name=Column(String(100),unique=True)
    exam_date=Column(Date)
    difficulty=Column(String(100))
    estimated_hours=Column(Integer)
    syllabus_topics=Column(Text)
    created_at=Column(DateTime, default=datetime.today)