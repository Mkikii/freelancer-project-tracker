from models import Client, Project, TimeEntry, Category, get_session
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

def seed_database():
    """Seed the database with sample data"""
    session = get_session()
    
    try:
        session.query(TimeEntry).delete()
        session.query(Project).delete()
        session.query(Client).delete()
        session.query(Category).delete()
        
       
        categories_data = [
            ("Web Development", "Website and web application development", "#FF5733"),
            ("Mobile Development", "Mobile app development", "#33FF57"),
            ("UI/UX Design", "User interface and experience design", "#3357FF"),
            ("Content Writing", "Blog posts, articles, and copywriting", "#F333FF"),
            ("Digital Marketing", "SEO, social media, and online advertising", "#FF33A1")
        ]
        
        categories = []
        for name, description, color in categories_data:
            category = Category(
                name=name,
                description=description,
                color_code=color
            )
            categories.append(category)
            session.add(category)
        
        session.commit()
        
        clients = []
        for _ in range(10):
            client = Client(
                name=fake.company(),
                email=fake.email(),
                company=fake.company(),
                phone=fake.phone_number(),
                notes=fake.paragraph()
            )
            clients.append(client)
            session.add(client)
        
        session.commit()
        
        projects = []
        for client in clients:
            for _ in range(random.randint(1, 3)):
                project = Project(
                    name=fake.catch_phrase(),
                    description=fake.paragraph(),
                    hourly_rate=round(random.uniform(25, 100), 2),
                    status=random.choice(['active', 'completed', 'paused']),
                    deadline=fake.future_date(),
                    client_id=client.id,
                    category_id=random.choice(categories).id
                )
                projects.append(project)
                session.add(project)
        
        session.commit()
       
        for project in projects:
            for _ in range(random.randint(5, 20)):
                entry_date = fake.date_between(start_date='-60d', end_date='today')
                hours = round(random.uniform(0.5, 8), 2)
                
                time_entry = TimeEntry(
                    date=entry_date,
                    hours_worked=hours,
                    description=fake.sentence(),
                    task_type=random.choice(['coding', 'design', 'meeting', 'research', 'testing']),
                    project_id=project.id
                )
                session.add(time_entry)
        
        session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"📊 Created: {len(categories)} categories, {len(clients)} clients, {len(projects)} projects")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error seeding database: {str(e)}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()