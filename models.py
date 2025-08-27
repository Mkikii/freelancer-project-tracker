# models.py - Database Models for Freelancer Project & Time Tracker
# Created by: Maureen W Karimi
# Phase 3 Python CLI Project - Moringa School

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Create database base class
Base = declarative_base()

class Client(Base):
    """Client model - represents freelance clients"""
    __tablename__ = 'clients'
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Client information (4+ attributes as required)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    company = Column(String(100))
    phone = Column(String(20))
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    
    # One-to-Many relationship: One client can have many projects
    projects = relationship("Project", back_populates="client")
    
    def __repr__(self):
        return f"<Client(name='{self.name}', company='{self.company}')>"
    
    # Method to get total earnings from this client
    def get_total_earnings(self):
        total = 0
        for project in self.projects:
            total += project.get_total_earnings()
        return total

class Project(Base):
    """Project model - represents freelance projects"""
    __tablename__ = 'projects'
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Project information (4+ attributes as required)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    hourly_rate = Column(Float, nullable=False, default=25.0)  # Default $25/hour
    status = Column(String(20), default='active')  # active, completed, paused
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)
    
    # Foreign key to link to client
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    
    # Relationships
    client = relationship("Client", back_populates="projects")
    time_entries = relationship("TimeEntry", back_populates="project")
    
    def __repr__(self):
        return f"<Project(name='{self.name}', rate=${self.hourly_rate}/hr)>"
    
    # Method to calculate total hours worked
    def get_total_hours(self):
        return sum(entry.hours_worked for entry in self.time_entries)
    
    # Method to calculate total earnings
    def get_total_earnings(self):
        return self.get_total_hours() * self.hourly_rate

class TimeEntry(Base):
    """Time Entry model - tracks work sessions"""
    __tablename__ = 'time_entries'
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Time entry information (4+ attributes as required)
    date = Column(DateTime, default=datetime.now)
    hours_worked = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    task_type = Column(String(50))  # coding, design, meeting, etc.
    created_at = Column(DateTime, default=datetime.now)
    
    # Foreign key to link to project
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    
    # Relationships
    project = relationship("Project", back_populates="time_entries")
    
    def __repr__(self):
        return f"<TimeEntry(hours={self.hours_worked}, date={self.date.date()})>"
    
    # Method to calculate earnings for this entry
    def get_earnings(self):
        return self.hours_worked * self.project.hourly_rate

class Category(Base):
    """Category model - for organizing different types of work"""
    __tablename__ = 'categories'
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Category information (4+ attributes as required)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    color_code = Column(String(7))  # Hex color code like #FF5733
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Category(name='{self.name}')>"

# Database setup
engine = create_engine('sqlite:///freelancer_tracker.db', echo=False)

def init_db():
    """Initialize the database - create all tables"""
    Base.metadata.create_all(engine)
    print("📊 Database initialized successfully!")

# Create session factory
SessionLocal = sessionmaker(bind=engine)

# Helper function to get database session
def get_session():
    return SessionLocal()

if __name__ == "__main__":
    # Initialize database when running this file directly
    init_db()
    print("✅ Database models created successfully!")
    print("Run 'python cli.py' to start the application!")