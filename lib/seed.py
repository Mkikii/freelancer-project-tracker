from lib.models import Session, Client, Project, TimeEntry
from datetime import datetime, timedelta

def seed_database():
    session = Session()
    
    client1 = Client(
        name="John Doe",
        email="john@example.com",
        company="ABC Corp",
        phone="123-456-7890",
        hourly_rate=75.0
    )
    
    client2 = Client(
        name="Jane Smith",
        email="jane@example.com",
        company="XYZ Inc",
        phone="098-765-4321",
        hourly_rate=100.0
    )
    
    session.add_all([client1, client2])
    session.commit()
    
    project1 = Project(
        name="Website Redesign",
        description="Redesign company website",
        client_id=client1.id,
        hourly_rate=85.0,
        status="active",
        deadline=datetime.now() + timedelta(days=30)
    )
    
    project2 = Project(
        name="Mobile App Development",
        description="Develop mobile application",
        client_id=client2.id,
        hourly_rate=120.0,
        status="in-progress",
        deadline=datetime.now() + timedelta(days=60)
    )
    
    session.add_all([project1, project2])
    session.commit()
    
    time_entry1 = TimeEntry(
        project_id=project1.id,
        hours=5.5,
        description="Homepage design",
        task_type="Design",
        date_worked=datetime.now() - timedelta(days=2)
    )
    
    time_entry2 = TimeEntry(
        project_id=project2.id,
        hours=8.0,
        description="API integration",
        task_type="Development",
        date_worked=datetime.now() - timedelta(days=1)
    )
    
    session.add_all([time_entry1, time_entry2])
    session.commit()
    session.close()
    
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()