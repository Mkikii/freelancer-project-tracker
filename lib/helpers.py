import re
from datetime import datetime
from lib.models import Session, Client, Project

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^[\d\s\-\+\(\)]{10,}$'
    return re.match(pattern, phone) is not None

def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        try:
            datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            try:
                datetime.strptime(date_string, '%m-%d-%Y')
                return True
            except ValueError:
                return False

def parse_date(date_string):
    formats = ['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return None

def format_currency(amount):
    return f"${amount:.2f}"

def format_date(date_obj):
    return date_obj.strftime('%Y-%m-%d') if date_obj else "N/A"

def get_client_summary():
    session = Session()
    clients = session.query(Client).all()
    
    client_data = []
    for client in clients:
        total_projects = len(client.projects)
        total_hours = sum(entry.hours for entry in client.time_entries)
        total_earnings = sum(entry.hours * client.hourly_rate for entry in client.time_entries)
        
        client_data.append({
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'company': client.company,
            'hourly_rate': client.hourly_rate,
            'projects_count': total_projects,
            'total_hours': total_hours,
            'total_earnings': total_earnings
        })
    
    session.close()
    return client_data

def get_project_summary():
    session = Session()
    projects = session.query(Project).all()
    
    summary = []
    for project in projects:
        total_hours = sum(entry.hours for entry in project.time_entries)
        total_earnings = total_hours * project.hourly_rate
        
        summary.append({
            'id': project.id,
            'name': project.name,
            'client': project.client.name,
            'hourly_rate': project.hourly_rate,
            'status': project.status,
            'total_hours': total_hours,
            'total_earnings': total_earnings,
            'deadline': project.deadline
        })
    
    session.close()
    return summary