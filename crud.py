from models import Client, Project, TimeEntry, Session
from datetime import datetime

def create_client(name, email, phone, company, rate):
    session = Session()
    try:
        client = Client(name=name, email=email, phone=phone, company=company, hourly_rate=rate)
        session.add(client)
        session.commit()
        return f"Added client: {name}"
    except:
        session.rollback()
        return "Error: Client may already exist"
    finally:
        session.close()

def get_all_clients():
    session = Session()
    clients = session.query(Client).all()
    session.close()
    return clients

def create_project(name, client_id, rate, deadline):
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    if not client:
        session.close()
        return "Error: Client not found"
    deadline_date = None
    if deadline:
        try:
            deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
        except:
            session.close()
            return "Error: Invalid date format"
    try:
        project = Project(name=name, client_id=client_id, project_rate=rate, deadline=deadline_date)
        session.add(project)
        session.commit()
        return f"Added project: {name} for {client.name}"
    except:
        session.rollback()
        return "Error adding project"
    finally:
        session.close()

def get_all_projects():
    session = Session()
    projects = session.query(Project).all()
    session.close()
    return projects

def log_time(description, hours, client_id, project_id):
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    project = session.query(Project).filter_by(id=project_id).first()
    if not client or not project:
        session.close()
        return "Error: Client or Project not found"
    try:
        time_entry = TimeEntry(description=description, hours=hours, client_id=client_id, project_id=project_id)
        session.add(time_entry)
        session.commit()
        rate = project.project_rate or client.hourly_rate
        earnings = hours * rate
        return f"Logged {hours} hours - ${earnings:.2f} earned"
    except:
        session.rollback()
        return "Error logging time"
    finally:
        session.close()

def generate_time_report(client_id=None, project_id=None):
    session = Session()
    query = session.query(TimeEntry)
    if client_id:
        query = query.filter_by(client_id=client_id)
    if project_id:
        query = query.filter_by(project_id=project_id)
    time_entries = query.all()
    session.close()
    return time_entries

def generate_earnings_report(client_id=None, start_date=None, end_date=None):
    session = Session()
    query = session.query(TimeEntry)
    if client_id:
        query = query.filter_by(client_id=client_id)
    if start_date:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        query = query.filter(TimeEntry.date >= start)
    if end_date:
        end = datetime.strptime(end_date, '%Y-%m-%d')
        query = query.filter(TimeEntry.date <= end)
    time_entries = query.all()
    session.close()
    return time_entries