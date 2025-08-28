import click
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from models import engine, Client, Project, TimeEntry, Category, init_db
from crud import (
    add_client, get_all_clients, get_client_by_id, update_client, delete_client,
    add_project, get_all_projects, get_project_by_id, update_project_status, delete_project,
    add_time_entry, get_recent_time_entries, get_all_time_entries, update_time_entry, delete_time_entry,
    add_category, get_all_categories, get_category_by_id,
    get_business_summary, get_client_earnings
)
from tabulate import tabulate
from seed import seed_database
from debug import debug_database

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """💼 Freelancer Project & Time Tracker by Maureen W Karimi
    
    Manage your freelance business with ease! Track clients, projects, and time worked.
    """

    init_db()

@cli.command()
def seed():
    """🌱 Seed the database with sample data"""
    if click.confirm("This will delete all existing data. Are you sure?"):
        seed_database()
    else:
        click.echo("Seeding cancelled.")

@cli.command()
def debug():
    """🔧 Show database debug information"""
    debug_database()

@cli.group()
def client():
    """👥 Manage your clients"""
    pass

@client.command()
@click.option('--name', prompt='Client name', help='Name of the client')
@click.option('--email', prompt='Email address', help='Client email address')
@click.option('--company', prompt='Company (optional)', default='', help='Company name')
@click.option('--phone', prompt='Phone (optional)', default='', help='Phone number')
def add(name, email, company, phone):
    """Add a new client to your business"""
    success, message = add_client(
        name, email, 
        company if company else None, 
        phone if phone else None
    )
    
    if success:
        click.echo(f"✅ {message}")
    else:
        click.echo(f"❌ {message}")

@client.command()
def list():
    """View all your clients"""
    clients = get_all_clients()
    
    if not clients:
        click.echo("📭 No clients found. Add your first client with 'python cli.py client add'")
        return
    
    table_data = []
    for client in clients:
        projects_count = len(client.projects)
        total_earnings = client.get_total_earnings()
        
        table_data.append([
            client.id,
            client.name,
            client.company or "N/A",
            client.email,
            projects_count,
            f"${total_earnings:.2f}"
        ])
    
    headers = ["ID", "Name", "Company", "Email", "Projects", "Total Earned"]
    click.echo("\n👥 YOUR CLIENTS:")
    click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))

@client.command()
@click.argument('client_id', type=int)
def view(client_id):
    """View details of a specific client"""
    client = get_client_by_id(client_id)
    
    if not client:
        click.echo(f"❌ Client with ID {client_id} not found!")
        return
    
    click.echo(f"\n👥 CLIENT DETAILS: {client.name}")
    click.echo(f"📧 Email: {client.email}")
    click.echo(f"🏢 Company: {client.company or 'N/A'}")
    click.echo(f"📞 Phone: {client.phone or 'N/A'}")
    click.echo(f"📅 Created: {client.created_at.strftime('%Y-%m-%d')}")
    
    if client.notes:
        click.echo(f"📝 Notes: {client.notes}")
    
    if client.projects:
        click.echo(f"\n📁 PROJECTS ({len(client.projects)}):")
        table_data = []
        for project in client.projects:
            total_hours = project.get_total_hours()
            total_earnings = project.get_total_earnings()
            
            table_data.append([
                project.id,
                project.name,
                f"${project.hourly_rate:.2f}",
                f"{total_hours:.1f}h",
                f"${total_earnings:.2f}",
                project.status.upper()
            ])
        
        headers = ["ID", "Project", "Rate/hr", "Hours", "Earned", "Status"]
        click.echo(tabulate(table_data, headers=headers, tablefmt="simple"))
    
    total_earnings = client.get_total_earnings()
    click.echo(f"\n💰 TOTAL EARNED FROM CLIENT: ${total_earnings:.2f}")

@cli.group()
def project():
    """📁 Manage your projects"""
    pass

@project.command()
@click.option('--name', prompt='Project name', help='Name of the project')
@click.option('--client-id', prompt='Client ID', type=int, help='ID of the client')
@click.option('--rate', prompt='Hourly rate ($)', type=float, default=25.0, help='Hourly rate in dollars')
@click.option('--description', prompt='Description (optional)', default='', help='Project description')
@click.option('--category-id', prompt='Category ID (optional)', default=None, type=int, help='Category ID')
def add(name, client_id, rate, description, category_id):
    """Create a new project"""
    success, message = add_project(
        name, client_id, rate,
        description if description else None,
        category_id if category_id else None
    )
    
    if success:
        click.echo(f"✅ {message}")
    else:
        click.echo(f"❌ {message}")

@project.command()
def list():
    """View all your projects"""
    projects = get_all_projects()
    
    if not projects:
        click.echo("📭 No projects found. Create your first project with 'python cli.py project add'")
        return
    
    table_data = []
    for project in projects:
        total_hours = project.get_total_hours()
        total_earnings = project.get_total_earnings()
        
        table_data.append([
            project.id,
            project.name,
            project.client.name,
            f"${project.hourly_rate:.2f}",
            f"{total_hours:.1f}h",
            f"${total_earnings:.2f}",
            project.status.upper()
        ])
    
    headers = ["ID", "Project", "Client", "Rate/hr", "Hours", "Earned", "Status"]
    click.echo("\n📁 YOUR PROJECTS:")
    click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))

@project.command()
@click.argument('project_id', type=int)
def view(project_id):
    """View details of a specific project"""
    project = get_project_by_id(project_id)
    
    if not project:
        click.echo(f"❌ Project with ID {project_id} not found!")
        return
    
    click.echo(f"\n📁 PROJECT DETAILS: {project.name}")
    click.echo(f"👥 Client: {project.client.name}")
    click.echo(f"💰 Hourly Rate: ${project.hourly_rate:.2f}")
    click.echo(f"📊 Status: {project.status.upper()}")
    click.echo(f"📅 Created: {project.created_at.strftime('%Y-%m-%d')}")
    
    if project.description:
        click.echo(f"📝 Description: {project.description}")
    
    if project.deadline:
        click.echo(f"⏰ Deadline: {project.deadline.strftime('%Y-%m-%d')}")
    
    if project.category:
        click.echo(f"🏷️ Category: {project.category.name}")
    
    if project.time_entries:
        click.echo(f"\n⏰ TIME ENTRIES ({len(project.time_entries)}):")
        table_data = []
        for entry in project.time_entries[:10]:
            table_data.append([
                entry.date.strftime('%Y-%m-%d'),
                f"{entry.hours_worked:.2f}h",
                entry.description[:40] + "..." if len(entry.description) > 40 else entry.description,
                f"${entry.get_earnings():.2f}"
            ])
        
        headers = ["Date", "Hours", "Description", "Earned"]
        click.echo(tabulate(table_data, headers=headers, tablefmt="simple"))
   
    total_hours = project.get_total_hours()
    total_earnings = project.get_total_earnings()
    click.echo(f"\n📊 TOTALS: {total_hours:.2f} hours | 💰 ${total_earnings:.2f}")

@project.command()
@click.argument('project_id', type=int)
@click.option('--status', type=click.Choice(['active', 'completed', 'paused']), 
              prompt='New status', help='New project status')
def status(project_id, status):
    """Update project status"""
    success, message = update_project_status(project_id, status)
    
    if success:
        click.echo(f"✅ {message}")
    else:
        click.echo(f"❌ {message}")

@cli.group()
def time():
    """⏰ Track your work time"""
    pass

@time.command()
@click.option('--project-id', prompt='Project ID', type=int, help='ID of the project')
@click.option('--hours', prompt='Hours worked', type=float, help='Number of hours worked')
@click.option('--description', prompt='What did you work on?', help='Description of work done')
@click.option('--task-type', prompt='Task type (optional)', default='', help='Type of task (coding, design, meeting, etc.)')
def log(project_id, hours, description, task_type):
    """Log time worked on a project"""
    success, message = add_time_entry(
        project_id, hours, description,
        task_type if task_type else None
    )
    
    if success:
        click.echo(f"✅ {message}")
    else:
        click.echo(f"❌ {message}")

@time.command()
@click.option('--days', default=7, help='Number of days to show (default: 7)')
def recent(days):
    """View recent time entries"""
    entries = get_recent_time_entries(days)
    
    if not entries:
        click.echo(f"📭 No time entries found in the last {days} days")
        click.echo("💡 Log your first time entry with 'python cli.py time log'")
        return
    
    table_data = []
    total_hours = 0
    total_earnings = 0
    
    for entry in entries:
        earnings = entry.get_earnings()
        total_hours += entry.hours_worked
        total_earnings += earnings
        
        table_data.append([
            entry.date.strftime('%Y-%m-%d'),
            entry.project.name,
            f"{entry.hours_worked:.1f}h",
            entry.description[:50] + "..." if len(entry.description) > 50 else entry.description,
            f"${earnings:.2f}"
        ])
    
    headers = ["Date", "Project", "Hours", "Description", "Earned"]
    click.echo(f"\n⏰ TIME ENTRIES (Last {days} days):")
    click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
    click.echo(f"\n📊 TOTALS: {total_hours:.1f} hours | 💰 ${total_earnings:.2f}")

@cli.group()
def category():
    """🏷️ Manage work categories"""
    pass

@category.command()
@click.option('--name', prompt='Category name', help='Name of the category')
@click.option('--description', prompt='Description (optional)', default='', help='Category description')
@click.option('--color', prompt='Color code (optional)', default='', help='Hex color code (e.g., #FF5733)')
def add(name, description, color):
    """Add a new work category"""
    success, message = add_category(
        name,
        description if description else None,
        color if color else None
    )
    
    if success:
        click.echo(f"✅ {message}")
    else:
        click.echo(f"❌ {message}")

@category.command()
def list():
    """View all categories"""
    categories = get_all_categories()
    
    if not categories:
        click.echo("📭 No categories found. Add your first category with 'python cli.py category add'")
        return
    
    table_data = []
    for category in categories:
        projects_count = len(category.projects)
        
        table_data.append([
            category.id,
            category.name,
            category.description or "N/A",
            category.color_code or "N/A",
            projects_count
        ])
    
    headers = ["ID", "Name", "Description", "Color", "Projects"]
    click.echo("\n🏷️ CATEGORIES:")
    click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))

@cli.command()
def summary():
    """📈 View business summary"""
    summary = get_business_summary()
    
    if not summary:
        click.echo("❌ Error generating business summary!")
        return
    
    click.echo("\n" + "="*50)
    click.echo("📈 FREELANCE BUSINESS SUMMARY")
    click.echo("="*50)
    click.echo(f"👥 Total Clients: {summary['total_clients']}")
    click.echo(f"📁 Total Projects: {summary['total_projects']}")
    click.echo(f"⏰ Total Hours Worked: {summary['total_hours']:.1f}")
    click.echo(f"💰 Total Earnings: ${summary['total_earnings']:.2f}")
    click.echo("\n" + "-"*30)
    
    now = datetime.now()
    click.echo(f"📅 This Month ({now.strftime('%B %Y')}):")
    click.echo(f"⏰ Hours: {summary['month_hours']:.1f}")
    click.echo(f"💰 Earnings: ${summary['month_earnings']:.2f}")
    
    if summary['total_hours'] > 0:
        click.echo(f"📊 Average Rate: ${summary['avg_rate']:.2f}/hour")
    
    click.echo("="*50)

@cli.command()
@click.option('--days', default=30, help='Time period in days (default: 30)')
def report(days):
    """📊 Generate a detailed business report"""
    click.echo(f"\n📊 BUSINESS REPORT (Last {days} days)")
    click.echo("="*60)
    
    cutoff_date = datetime.now() - timedelta(days=days)
    session = Session()
    
    try:
        entries = session.query(TimeEntry).filter(
            TimeEntry.date >= cutoff_date
        ).order_by(TimeEntry.date.desc()).all()
        
        if not entries:
            click.echo("No time entries found for this period.")
            return
       
        total_hours = sum(entry.hours_worked for entry in entries)
        total_earnings = sum(entry.get_earnings() for entry in entries)
       
        projects = {}
        for entry in entries:
            project_id = entry.project_id
            if project_id not in projects:
                projects[project_id] = {
                    'name': entry.project.name,
                    'client': entry.project.client.name,
                    'hours': 0,
                    'earnings': 0
                }
            
            projects[project_id]['hours'] += entry.hours_worked
            projects[project_id]['earnings'] += entry.get_earnings()
        
        click.echo(f"📅 Period: {cutoff_date.strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}")
        click.echo(f"⏰ Total Hours: {total_hours:.2f}")
        click.echo(f"💰 Total Earnings: ${total_earnings:.2f}")
        click.echo("\n" + "-"*60)
        
        if projects:
            click.echo("📁 PROJECT BREAKDOWN:")
            table_data = []
            for project_id, data in projects.items():
                table_data.append([
                    data['name'],
                    data['client'],
                    f"{data['hours']:.2f}h",
                    f"${data['earnings']:.2f}"
                ])
            
            headers = ["Project", "Client", "Hours", "Earnings"]
            click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
      
        daily_data = {}
        for entry in entries:
            date_str = entry.date.strftime('%Y-%m-%d')
            if date_str not in daily_data:
                daily_data[date_str] = {
                    'hours': 0,
                    'earnings': 0
                }
            
            daily_data[date_str]['hours'] += entry.hours_worked
            daily_data[date_str]['earnings'] += entry.get_earnings()
        
        click.echo("\n📅 DAILY BREAKDOWN:")
        table_data = []
        for date_str, data in sorted(daily_data.items(), reverse=True):
            table_data.append([
                date_str,
                f"{data['hours']:.2f}h",
                f"${data['earnings']:.2f}"
            ])
        
        headers = ["Date", "Hours", "Earnings"]
        click.echo(tabulate(table_data, headers=headers, tablefmt="simple"))
        
    except Exception as e:
        click.echo(f"❌ Error generating report: {str(e)}")
    finally:
        session.close()

if __name__ == '__main__':
    cli()