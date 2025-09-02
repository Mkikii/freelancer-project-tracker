from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    hourly_rate = Column(Float, default=50.0)
    projects = relationship("Project", back_populates="client")
    time_entries = relationship("TimeEntry", back_populates="client")

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))
    project_rate = Column(Float)
    deadline = Column(DateTime)
    client = relationship("Client", back_populates="projects")
    time_entries = relationship("TimeEntry", back_populates="project")

class TimeEntry(Base):
    __tablename__ = 'time_entries'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    hours = Column(Float)
    date = Column(DateTime, default=datetime.now)
    client_id = Column(Integer, ForeignKey('clients.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))
    client = relationship("Client", back_populates="time_entries")
    project = relationship("Project", back_populates="time_entries")

db_path = os.path.join(os.path.dirname(__file__), '..', 'freelancer.db')
engine = create_engine(f'sqlite:///{os.path.abspath(db_path)}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
