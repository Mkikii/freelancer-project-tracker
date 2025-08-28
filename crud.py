from models import Client, Project, TimeEntry, Category, get_session
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError

def add_client(name, email, company=None, phone=None):
    """Add a new client to the database"""
    session = get_session()
    try:
    
        existing_client = session.query(Client).filter_by(email=email).first()
        if existing_client:
            return False, f"Client with email {email} already exists!"
        
        new_client = Client(
            name=name,
            email=email,
            company=company,
            phone=phone
        )
        session.add(new_client)
        session.commit()
        return True, f"Client '{name}' added successfully!"
        
    except IntegrityError:
        session.rollback()
        return False, "Database integrity error occurred!"
    except Exception as e:
        session.rollback()
        return False, f"Error adding client: {str(e)}"
    finally:
        session.close()

def get_all_clients():
    """Get all clients from database"""
    session = get_session()
    try:
        clients = session.query(Client).all()
        return clients
    except Exception as e:
        print(f"Error fetching clients: {str(e)}")
        return []
    finally:
        session.close()

def get_client_by_id(client_id):
    """Get a specific client by ID"""
    session = get_session()
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        return client
    except Exception as e:
        print(f"Error fetching client: {str(e)}")
        return None
    finally:
        session.close()

def update_client(client_id, **kwargs):
    """Update client information"""
    session = get_session()
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        if not client:
            return False, f"Client with ID {client_id} not found!"
        
        for key, value in kwargs.items():
            if hasattr(client, key):
                setattr(client, key, value)
        
        session.commit()
        return True, f"Client '{client.name}' updated successfully!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error updating client: {str(e)}"
    finally:
        session.close()

def delete_client(client_id):
    """Delete a client"""
    session = get_session()
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        if not client:
            return False, f"Client with ID {client_id} not found!"
        
        session.delete(client)
        session.commit()
        return True, f"Client '{client.name}' deleted successfully!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error deleting client: {str(e)}"
    finally:
        session.close()

def add_project(name, client_id, hourly_rate, description=None, category_id=None):
    """Add a new project to the database"""
    session = get_session()
    try:
    
        client = session.query(Client).filter_by(id=client_id).first()
        if not client:
            return False, f"Client with ID {client_id} not found!"
        
        new_project = Project(
            name=name,
            client_id=client_id,
            hourly_rate=hourly_rate,
            description=description,
            category_id=category_id
        )
        session.add(new_project)
        session.commit()
        return True, f"Project '{name}' created for {client.name}!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error creating project: {str(e)}"
    finally:
        session.close()

def get_all_projects():
    """Get all projects from database"""
    session = get_session()
    try:
        projects = session.query(Project).all()
        return projects
    except Exception as e:
        print(f"Error fetching projects: {str(e)}")
        return []
    finally:
        session.close()

def get_project_by_id(project_id):
    """Get a specific project by ID"""
    session = get_session()
    try:
        project = session.query(Project).filter_by(id=project_id).first()
        return project
    except Exception as e:
        print(f"Error fetching project: {str(e)}")
        return None
    finally:
        session.close()

def update_project_status(project_id, status):
    """Update project status"""
    session = get_session()
    try:
        project = session.query(Project).filter_by(id=project_id).first()
        if not project:
            return False, f"Project with ID {project_id} not found!"
        
        project.status = status
        session.commit()
        return True, f"Project status updated to '{status}'"
        
    except Exception as e:
        session.rollback()
        return False, f"Error updating project: {str(e)}"
    finally:
        session.close()

def delete_project(project_id):
    """Delete a project"""
    session = get_session()
    try:
        project = session.query(Project).filter_by(id=project_id).first()
        if not project:
            return False, f"Project with ID {project_id} not found!"
        
        session.delete(project)
        session.commit()
        return True, f"Project '{project.name}' deleted successfully!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error deleting project: {str(e)}"
    finally:
        session.close()

def add_time_entry(project_id, hours_worked, description, task_type=None):
    """Add a new time entry"""
    session = get_session()
    try:
        
        project = session.query(Project).filter_by(id=project_id).first()
        if not project:
            return False, f"Project with ID {project_id} not found!"
        
        new_entry = TimeEntry(
            project_id=project_id,
            hours_worked=hours_worked,
            description=description,
            task_type=task_type
        )
        session.add(new_entry)
        session.commit()
        
        earnings = hours_worked * project.hourly_rate
        return True, f"Time logged: {hours_worked}h on '{project.name}' - Earned ${earnings:.2f}!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error logging time: {str(e)}"
    finally:
        session.close()

def get_recent_time_entries(days=7):
    """Get time entries from the last N days"""
    session = get_session()
    try:
        cutoff_date = datetime.now() - timedelta(days=days)
        entries = session.query(TimeEntry).filter(
            TimeEntry.date >= cutoff_date
        ).order_by(TimeEntry.date.desc()).all()
        return entries
    except Exception as e:
        print(f"Error fetching time entries: {str(e)}")
        return []
    finally:
        session.close()

def get_all_time_entries():
    """Get all time entries"""
    session = get_session()
    try:
        entries = session.query(TimeEntry).all()
        return entries
    except Exception as e:
        print(f"Error fetching time entries: {str(e)}")
        return []
    finally:
        session.close()

def update_time_entry(entry_id, **kwargs):
    """Update a time entry"""
    session = get_session()
    try:
        entry = session.query(TimeEntry).filter_by(id=entry_id).first()
        if not entry:
            return False, f"Time entry with ID {entry_id} not found!"
        
        for key, value in kwargs.items():
            if hasattr(entry, key):
                setattr(entry, key, value)
        
        session.commit()
        return True, f"Time entry updated successfully!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error updating time entry: {str(e)}"
    finally:
        session.close()

def delete_time_entry(entry_id):
    """Delete a time entry"""
    session = get_session()
    try:
        entry = session.query(TimeEntry).filter_by(id=entry_id).first()
        if not entry:
            return False, f"Time entry with ID {entry_id} not found!"
        
        session.delete(entry)
        session.commit()
        return True, f"Time entry deleted successfully!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error deleting time entry: {str(e)}"
    finally:
        session.close()

def add_category(name, description=None, color_code=None):
    """Add a new category"""
    session = get_session()
    try:
        
        existing_category = session.query(Category).filter_by(name=name).first()
        if existing_category:
            return False, f"Category '{name}' already exists!"
        
        new_category = Category(
            name=name,
            description=description,
            color_code=color_code
        )
        session.add(new_category)
        session.commit()
        return True, f"Category '{name}' added successfully!"
        
    except Exception as e:
        session.rollback()
        return False, f"Error adding category: {str(e)}"
    finally:
        session.close()

def get_all_categories():
    """Get all categories"""
    session = get_session()
    try:
        categories = session.query(Category).filter_by(is_active=True).all()
        return categories
    except Exception as e:
        print(f"Error fetching categories: {str(e)}")
        return []
    finally:
        session.close()

def get_category_by_id(category_id):
    """Get a specific category by ID"""
    session = get_session()
    try:
        category = session.query(Category).filter_by(id=category_id).first()
        return category
    except Exception as e:
        print(f"Error fetching category: {str(e)}")
        return None
    finally:
        session.close()

def get_business_summary():
    """Get overall business summary"""
    session = get_session()
    try:
        clients = session.query(Client).all()
        projects = session.query(Project).all()
        time_entries = session.query(TimeEntry).all()
        
        total_clients = len(clients)
        total_projects = len(projects)
        total_hours = sum(entry.hours_worked for entry in time_entries)
        total_earnings = sum(entry.get_earnings() for entry in time_entries)
        
        now = datetime.now()
        month_start = datetime(now.year, now.month, 1)
        month_entries = session.query(TimeEntry).filter(
            TimeEntry.date >= month_start
        ).all()
        
        month_hours = sum(entry.hours_worked for entry in month_entries)
        month_earnings = sum(entry.get_earnings() for entry in month_entries)
        
        return {
            'total_clients': total_clients,
            'total_projects': total_projects,
            'total_hours': total_hours,
            'total_earnings': total_earnings,
            'month_hours': month_hours,
            'month_earnings': month_earnings,
            'avg_rate': total_earnings / total_hours if total_hours > 0 else 0
        }
        
    except Exception as e:
        print(f"Error generating summary: {str(e)}")
        return None
    finally:
        session.close()

def get_client_earnings(client_id):
    """Get total earnings from a specific client"""
    session = get_session()
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        if not client:
            return 0
        
        return client.get_total_earnings()
        
    except Exception as e:
        print(f"Error calculating client earnings: {str(e)}")
        return 0
    finally:
        session.close()