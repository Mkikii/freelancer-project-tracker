from models import Client, Project, TimeEntry, Category, get_session
from datetime import datetime, timedelta
import random

def seed_database_simple():
    """Simple seed function without Faker"""
    session = get_session()
    
    try:
        
        session.query(TimeEntry).delete()
        session.query(Project).delete()
        session.query(Client).delete()
        session.query(Category).delete()
        
       
        categories = [
            Category(name="Web Development", description="Website and web application development", color_code="#FF5733"),
            Category(name="Mobile Development", description="Mobile app development", color_code="#33FF57"),
            Category(name="UI/UX Design", description="User interface and experience design", color_code="#3357FF"),
        ]
        
        for category in categories:
            session.add(category)
        
        session.commit()
   
        clients = [
            Client(name="Acme Corp", email="contact@acme.com", company="Acme Corporation", phone="555-1234"),
            Client(name="XYZ Ltd", email="info@xyz.com", company="XYZ Limited", phone="555-5678"),
        ]
        
        for client in clients:
            session.add(client)
        
        session.commit()
        
        projects = [
            Project(name="Website Redesign", client_id=1, hourly_rate=75.0, description="Complete website redesign", category_id=1),
            Project(name="Mobile App", client_id=2, hourly_rate=85.0, description="iOS and Android app development", category_id=2),
        ]
        
        for project in projects:
            session.add(project)
        
        session.commit()
    
        time_entries = [
            TimeEntry(project_id=1, hours_worked=5.5, description="Homepage design", date=datetime.now() - timedelta(days=2)),
            TimeEntry(project_id=1, hours_worked=3.0, description="Contact page implementation", date=datetime.now() - timedelta(days=1)),
            TimeEntry(project_id=2, hours_worked=8.0, description="App architecture planning", date=datetime.now()),
        ]
        
        for entry in time_entries:
            session.add(entry)
        
        session.commit()
        
        print("✅ Database seeded successfully with simple data!")
        print(f"📊 Created: {len(categories)} categories, {len(clients)} clients, {len(projects)} projects, {len(time_entries)} time entries")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error seeding database: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        session.close()

if __name__ == "__main__":
    seed_database_simple()