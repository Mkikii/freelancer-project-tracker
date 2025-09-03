import click
from lib.crud import (
    create_client, get_all_clients,
    create_project, get_all_projects,
    log_time, generate_time_report,
    generate_earnings_report
)
from lib.helpers import validate_email

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
    message = create_client(name, email, phone, company, rate)
    click.echo(message)

@cli.command()
def list_clients():
    clients = get_all_clients()
    for client in clients:
        click.echo(f"{client.id}: {client.name} - {client.email} - {client.company} (${client.hourly_rate}/hr)")

@cli.command()
@click.option('--name', prompt='Project name')
@click.option('--client-id', prompt='Client ID', type=int)
@click.option('--rate', type=float, help='Project rate')
@click.option('--deadline', help='Deadline YYYY-MM-DD')
def add_project(name, client_id, rate, deadline):
    message = create_project(name, client_id, rate, deadline)
    click.echo(message)

@cli.command()
def list_projects():
    projects = get_all_projects()
    for project in projects:
        click.echo(f"{project.id}: {project.name} - Client: {project.client.name}")

@cli.command()
@click.option('--description', prompt='Work description')
@click.option('--hours', prompt='Hours worked', type=float)
@click.option('--client-id', prompt='Client ID', type=int)
@click.option('--project-id', prompt='Project ID', type=int)
def log_time_entry(description, hours, client_id, project_id):
    message = log_time(description, hours, client_id, project_id)
    click.echo(message)

@cli.command()
@click.option('--client-id', type=int)
@click.option('--project-id', type=int)
def time_report(client_id, project_id):
    entries = generate_time_report(client_id, project_id)
    if not entries:
        click.echo("No time entries found")
        return
    total_hours = 0
    total_earnings = 0
    for entry in entries:
        rate = entry.project.project_rate or entry.client.hourly_rate
        earnings = entry.hours * rate
        total_hours += entry.hours
        total_earnings += earnings
        click.echo(f"{entry.date.date()} | {entry.client.name} | {entry.description} - {entry.hours} hrs - ${earnings:.2f}")
    click.echo(f"TOTAL: {total_hours} hours - ${total_earnings:.2f}")

@cli.command()
@click.option('--client-id', type=int)
@click.option('--start-date', help='YYYY-MM-DD')
@click.option('--end-date', help='YYYY-MM-DD')
def earnings_report(client_id, start_date, end_date):
    entries = generate_earnings_report(client_id, start_date, end_date)
    if not entries:
        click.echo("No time entries found")
        return
    client_earnings = {}
    total_earnings = 0
    for entry in entries:
        rate = entry.project.project_rate or entry.client.hourly_rate
        earnings = entry.hours * rate
        if entry.client.name not in client_earnings:
            client_earnings[entry.client.name] = {'hours': 0, 'earnings': 0}
        client_earnings[entry.client.name]['hours'] += entry.hours
        client_earnings[entry.client.name]['earnings'] += earnings
        total_earnings += earnings
    for client, data in client_earnings.items():
        click.echo(f"{client}: {data['hours']} hrs - ${data['earnings']:.2f}")
    click.echo(f"TOTAL EARNINGS: ${total_earnings:.2f}")

if __name__ == '__main__':
    cli()