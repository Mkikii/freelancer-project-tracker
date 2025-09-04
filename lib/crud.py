from sqlalchemy.orm import joinedload
from lib.models import Session, Client, Project, TimeEntry
from datetime import datetime

def create_client(name, email, company, phone, hourly_rate):
    session = Session()
    client = Client(name=name, email=email, company=company, phone=phone, hourly_rate=hourly_rate)
    session.add(client)
    session.commit()
    session.close()
    return f"Client {name} created successfully"

def get_all_clients():
    session = Session()
    clients = session.query(Client).all()
    session.close()
    return clients

def get_client_by_id(client_id):
    session = Session()
    client = session.query(Client).filter(Client.id == client_id).first()
    session.close()
    return client

def create_project(name, client_id, description, hourly_rate, status, deadline):
    session = Session()
    project = Project(
        name=name, 
        client_id=client_id, 
        description=description, 
        hourly_rate=hourly_rate,
        status=status,
        deadline=deadline
    )
    session.add(project)
    session.commit()
    session.close()
    return f"Project {name} created successfully"

def get_all_projects():
    session = Session()
    projects = session.query(Project).options(joinedload(Project.client)).all()
    session.close()
    return projects

def get_projects_by_client(client_id):
    session = Session()
    projects = session.query(Project).filter(Project.client_id == client_id).all()
    session.close()
    return projects

def log_time(project_id, hours, description, task_type, date_worked):
    session = Session()
    time_entry = TimeEntry(
        project_id=project_id, 
        hours=hours, 
        description=description,
        task_type=task_type,
        date_worked=date_worked
    )
    session.add(time_entry)
    session.commit()
    session.close()
    return f"Time logged successfully: {hours} hours"

def get_time_entries(project_id=None):
    session = Session()
    if project_id:
        entries = session.query(TimeEntry).options(joinedload(TimeEntry.project)).filter(TimeEntry.project_id == project_id).all()
    else:
        entries = session.query(TimeEntry).options(joinedload(TimeEntry.project)).all()
    session.close()
    return entries

def get_earnings_report(client_id=None):
    session = Session()
    
    if client_id:
        projects = session.query(Project).options(joinedload(Project.client)).filter(Project.client_id == client_id).all()
    else:
        projects = session.query(Project).options(joinedload(Project.client)).all()
    
    report_data = []
    total_earnings = 0
    total_hours = 0
    
    for project in projects:
        project_hours = sum(entry.hours for entry in project.time_entries)
        project_earnings = project_hours * project.hourly_rate
        total_hours += project_hours
        total_earnings += project_earnings
        
        report_data.append({
            'project_name': project.name,
            'client_name': project.client.name,
            'hours': project_hours,
            'earnings': project_earnings
        })
    
    session.close()
    
    return {
        'entries': report_data,
        'total_hours': total_hours,
        'total_earnings': total_earnings
    }