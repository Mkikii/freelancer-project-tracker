from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    company = Column(String(100))
    phone = Column(String(20))
    hourly_rate = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    projects = relationship("Project", back_populates="client")

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    hourly_rate = Column(Float, nullable=False)
    status = Column(String(50), default='active')
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)
    
    client = relationship("Client", back_populates="projects")
    time_entries = relationship("TimeEntry", back_populates="project")

class TimeEntry(Base):
    __tablename__ = 'time_entries'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    date_worked = Column(DateTime, nullable=False, default=datetime.now)
    hours = Column(Float, nullable=False)
    description = Column(Text)
    task_type = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)
    
    project = relationship("Project", back_populates="time_entries")

engine = create_engine('sqlite:///freelancer.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)