import click
from datetime import datetime
from lib.crud import (
    create_client, get_all_clients, get_client_by_id,
    create_project, get_all_projects, get_projects_by_client,
    log_time, get_time_entries, get_earnings_report
)
from lib.helpers import validate_email, validate_date, parse_date, format_currency, format_date
from lib.seed import seed_database

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Client name')
@click.option('--email', prompt='Client email')
@click.option('--company', prompt='Company (optional)', default='')
@click.option('--phone', prompt='Phone (optional)', default='')
@click.option('--rate', prompt='Hourly rate', type=float)
def add_client(name, email, company, phone, rate):
    if not validate_email(email):
        click.echo("Error: Invalid email format")
        return
        
    result = create_client(name, email, company, phone, rate)
    click.echo(result)

@cli.command()
def list_clients():
    clients = get_all_clients()
    
    if not clients:
        click.echo("No clients found.")
        return
    
    click.echo("\nClients:")
    click.echo("-" * 50)
    for client in clients:
        click.echo(f"ID: {client.id} | Name: {client.name} | Email: {client.email} | Rate: ${client.hourly_rate}/hr")

@cli.command()
@click.option('--name', prompt='Project name')
@click.option('--client-id', prompt='Client ID', type=int)
@click.option('--description', prompt='Description (optional)', default='')
@click.option('--rate', prompt='Hourly rate', type=float)
@click.option('--status', prompt='Status', type=click.Choice(['active', 'completed', 'on-hold']), default='active')
@click.option('--deadline', prompt='Deadline (YYYY-MM-DD, optional)', default='')
def add_project(name, client_id, description, rate, status, deadline):
    client = get_client_by_id(client_id)
    if not client:
        click.echo("Error: Client not found.")
        return
    
    deadline_date = None
    if deadline:
        if not validate_date(deadline):
            click.echo("Error: Invalid date format. Use YYYY-MM-DD, DD-MM-YYYY, or MM-DD-YYYY.")
            return
        deadline_date = parse_date(deadline)
    
    result = create_project(name, client_id, description, rate, status, deadline_date)
    click.echo(result)

@cli.command()
def list_projects():
    projects = get_all_projects()
    
    if not projects:
        click.echo("No projects found.")
        return
    
    click.echo("\nProjects:")
    click.echo("-" * 70)
    for project in projects:
        deadline_str = project.deadline.strftime('%Y-%m-%d') if project.deadline else 'No deadline'
        click.echo(f"ID: {project.id} | Name: {project.name} | Client: {project.client.name} | Status: {project.status} | Deadline: {deadline_str}")

@cli.command()
@click.option('--project-id', prompt='Project ID', type=int)
@click.option('--hours', prompt='Hours worked', type=float)
@click.option('--description', prompt='Description of work')
@click.option('--task-type', prompt='Task type (optional)', default='')
@click.option('--date', prompt='Date worked (YYYY-MM-DD, today if empty)', default='')
def add_time(project_id, hours, description, task_type, date):
    projects = get_all_projects()
    project_exists = any(p.id == project_id for p in projects)
    if not project_exists:
        click.echo("Error: Project not found.")
        return
    
    if date.lower() in ['', 'today', 'now']:
        date_worked = datetime.now()
    else:
        date_worked = parse_date(date)
        if not date_worked:
            click.echo("Error: Invalid date format. Use YYYY-MM-DD, DD-MM-YYYY, or MM-DD-YYYY.")
            return
    
    result = log_time(project_id, hours, description, task_type, date_worked)
    click.echo(result)

@cli.command()
@click.option('--project-id', type=int, help='Filter by project ID')
def list_time(project_id):
    entries = get_time_entries(project_id)
    
    if not entries:
        click.echo("No time entries found.")
        return
    
    click.echo("\nTime Entries:")
    click.echo("-" * 60)
    for entry in entries:
        date_str = entry.date_worked.strftime('%Y-%m-%d')
        click.echo(f"Date: {date_str} | Project: {entry.project.name} | Hours: {entry.hours} | Task: {entry.description}")

@cli.command()
@click.option('--client-id', type=int, help='Filter by client ID')
def earnings_report(client_id):
    report = get_earnings_report(client_id)
    
    if not report['entries']:
        click.echo("No data found for earnings report.")
        return
    
    click.echo("\nEarnings Report:")
    click.echo("=" * 60)
    
    for entry in report['entries']:
        click.echo(f"Project: {entry['project_name']} | Client: {entry['client_name']} | Hours: {entry['hours']} | Earnings: ${entry['earnings']:.2f}")
    
    click.echo("-" * 60)
    click.echo(f"Total Hours: {report['total_hours']} | Total Earnings: ${report['total_earnings']:.2f}")

@cli.command()
def seed():
    seed_database()
    click.echo("Database seeded with sample data!")

if __name__ == '__main__':
    cli()