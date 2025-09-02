import click
from models import Client, Project, TimeEntry, Session
from helpers import validate_email, get_client_summary
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Client name')
@click.option('--email', prompt='Client email')
@click.option('--phone', prompt='Client phone', default='')
@click.option('--company', prompt='Client company', default='')
@click.option('--rate', prompt='Hourly rate', type=float, default=50.0)
def add_client(name, email, phone, company, rate):
    if not validate_email(email):
        click.echo("Error: Invalid email format")
        return
        
    session = Session()
    try:
        client = Client(name=name, email=email, phone=phone, company=company, hourly_rate=rate)
        session.add(client)
        session.commit()
        click.echo(f"Added client: {name}")
    except:
        session.rollback()
        click.echo("Error: Client may already exist")
    finally:
        session.close()

@cli.command()
def list_clients():
    session = Session()
    clients = session.query(Client).all()
    for client in clients:
        click.echo(f"{client.id}: {client.name} - {client.email} - {client.company} (${client.hourly_rate}/hr)")
    session.close()

@cli.command()
@click.option('--name', prompt='Project name')
@click.option('--client-id', prompt='Client ID', type=int)
@click.option('--rate', type=float, help='Project rate')
@click.option('--deadline', help='Deadline YYYY-MM-DD')
def add_project(name, client_id, rate, deadline):
    session = Session()
    client = session.query(Client).filter_by(id=client_id).first()
    
    if not client:
        click.echo("Error: Client not found")
        session.close()
        return
    
    deadline_date = None
    if deadline:
        try:
            deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
        except:
            click.echo("Error: Invalid date format")
            session.close()
            return
        
    try:
        project = Project(name=name, client_id=client_id, project_rate=rate, deadline=deadline_date)
        session.add(project)
        session.commit()
        click.echo(f"Added project: {name} for {client.name}")
    except:
        session.rollback()
        click.echo("Error adding project")
    finally:
        session.close()

@cli.command()
def list_projects():
    session = Session()
    projects = session.query(Project).all()
    for project in projects:
        click.echo(f"{project.id}: {project.name} - Client: {project.client.name}")
    session.close()

@cli.command()
@click.option('--description', prompt='Work description')
@click.option('--hours', prompt='Hours worked', type=float)
@click.option('--client-id', prompt='Client ID', type=int)
@click.option('--project-id', prompt='Project ID', type=int)
def log_time(description, hours, client_id, project_id):
    session = Session()
    
    client = session.query(Client).filter_by(id=client_id).first()
    project = session.query(Project).filter_by(id=project_id).first()
    
    if not client or not project:
        click.echo("Error: Client or Project not found")
        session.close()
        return
        
    try:
        time_entry = TimeEntry(description=description, hours=hours, client_id=client_id, project_id=project_id)
        session.add(time_entry)
        session.commit()
        rate = project.project_rate or client.hourly_rate
        earnings = hours * rate
        click.echo(f"Logged {hours} hours - ${earnings:.2f} earned")
    except:
        session.rollback()
        click.echo("Error logging time")
    finally:
        session.close()

@cli.command()
@click.option('--client-id', type=int)
@click.option('--project-id', type=int)
def time_report(client_id, project_id):
    session = Session()
    
    query = session.query(TimeEntry)
    if client_id:
        query = query.filter_by(client_id=client_id)
    if project_id:
        query = query.filter_by(project_id=project_id)
    
    time_entries = query.all()
    
    if not time_entries:
        click.echo("No time entries found")
        session.close()
        return
    
    total_hours = 0
    total_earnings = 0
    
    for entry in time_entries:
        rate = entry.project.project_rate or entry.client.hourly_rate
        earnings = entry.hours * rate
        total_hours += entry.hours
        total_earnings += earnings
        click.echo(f"{entry.date.date()} | {entry.client.name} | {entry.description} - {entry.hours} hrs - ${earnings:.2f}")
    
    click.echo(f"TOTAL: {total_hours} hours - ${total_earnings:.2f}")
    session.close()

@cli.command()
@click.option('--client-id', type=int)
@click.option('--start-date', help='YYYY-MM-DD')
@click.option('--end-date', help='YYYY-MM-DD')
def earnings_report(client_id, start_date, end_date):
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
    
    if not time_entries:
        click.echo("No time entries found")
        session.close()
        return
    
    client_earnings = {}
    for entry in time_entries:
        rate = entry.project.project_rate or entry.client.hourly_rate
        earnings = entry.hours * rate
        
        if entry.client.name not in client_earnings:
            client_earnings[entry.client.name] = {'hours': 0, 'earnings': 0}
        
        client_earnings[entry.client.name]['hours'] += entry.hours
        client_earnings[entry.client.name]['earnings'] += earnings
    
    total_earnings = 0
    for client, data in client_earnings.items():
        click.echo(f"{client}: {data['hours']} hrs - ${data['earnings']:.2f}")
        total_earnings += data['earnings']
    
    click.echo(f"TOTAL EARNINGS: ${total_earnings:.2f}")
    session.close()

if __name__ == '__main__':
    cli()