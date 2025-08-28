from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

Base = declarative_base()

class Client(Base):
    """Client model - represents freelance clients"""
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    company = Column(String(100))
    phone = Column(String(20))
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    
    projects = relationship("Project", back_populates="client")
    
    def __repr__(self):
        return f"<Client(name='{self.name}', company='{self.company}')>"
    
    def get_total_earnings(self):
        """Calculate total earnings from all client projects"""
        total = 0
        for project in self.projects:
            total += project.get_total_earnings()
        return total

class Project(Base):
    """Project model - represents freelance projects"""
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    hourly_rate = Column(Float, nullable=False, default=25.0)
    status = Column(String(20), default='active') 
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)
 
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    client = relationship("Client", back_populates="projects")
    time_entries = relationship("TimeEntry", back_populates="project")
    category = relationship("Category", back_populates="projects")
    
    def __repr__(self):
        return f"<Project(name='{self.name}', rate=${self.hourly_rate}/hr)>"
    
    def get_total_hours(self):
        """Calculate total hours worked on this project"""
        return sum(entry.hours_worked for entry in self.time_entries)
    
    def get_total_earnings(self):
        """Calculate total earnings from this project"""
        return self.get_total_hours() * self.hourly_rate

class TimeEntry(Base):
    """Time Entry model - tracks work sessions"""
    __tablename__ = 'time_entries'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.now)
    hours_worked = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    task_type = Column(String(50))  
    created_at = Column(DateTime, default=datetime.now)
    
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    
    project = relationship("Project", back_populates="time_entries")
    
    def __repr__(self):
        return f"<TimeEntry(hours={self.hours_worked}, date={self.date.date()})>"
    
    def get_earnings(self):
        """Calculate earnings for this time entry"""
        return self.hours_worked * self.project.hourly_rate

class Category(Base):
    """Category model - for organizing different types of work"""
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    color_code = Column(String(7))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
  
    projects = relationship("Project", back_populates="category")
    
    def __repr__(self):
        return f"<Category(name='{self.name}')>"

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///freelancer_tracker.db')
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    """Initialize the database - create all tables"""
    Base.metadata.create_all(engine)
    print("📊 Database initialized successfully!")

SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

if __name__ == "__main__":
  
    init_db()
    print("✅ Database models created successfully!")
    print("Run 'python cli.py' to start the application!")