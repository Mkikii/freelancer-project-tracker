import click
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from models import engine, Client, Project, TimeEntry, Category, init_db
from tabulate import tabulate

# Create database session
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """💼 Freelancer Project & Time Tracker by Maureen W Karimi
    
    Manage your freelance business with ease! Track clients, projects, and time worked.
    """
    # Initialize database on startup
    init_db()

# ================================
# CLIENT MANAGEMENT COMMANDS
# ================================

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
    session = Session()
    try:
        # Check if client already exists
        existing_client = session.query(Client).filter_by(email=email).first()
        if existing_client:
            click.echo(f"❌ Client with email {email} already exists!")
            return
        
        # Create new client
        new_client = Client(
            name=name,
            email=email,
            company=company if company else None,
            phone=phone if phone else None
        )
        
        session.add(new_client)
        session.commit()
        
        click.echo(f"✅ Client '{name}' added successfully!")
        click.echo("💡 Tip: Use 'python cli.py project add' to create a project for this client")
        
    except Exception as e:
        session.rollback()
        click.echo(f"❌ Error adding client: {str(e)}")
    finally:
        session.close()

@client.command()
def list():
    """View all your clients"""
    session = Session()
    try:
        clients = session.query(Client).all()
        
        if not clients:
            click.echo("📭 No clients found. Add your first client with 'python cli.py client add'")
            return
        
        # Prepare data for table
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
        
    except Exception as e:
        click.echo(f"❌ Error fetching clients: {str(e)}")
    finally:
        session.close()

# ================================
# PROJECT MANAGEMENT COMMANDS
# ================================

@cli.group()
def project():
    """📁 Manage your projects"""
    pass

@project.command()
@click.option('--name', prompt='Project name', help='Name of the project')
@click.option('--client-id', prompt='Client ID', type=int, help='ID of the client')
@click.option('--rate', prompt='Hourly rate ($)', type=float, default=25.0, help='Hourly rate in dollars')
@click.option('--description', prompt='Description (optional)', default='', help='Project description')
def add(name, client_id, rate, description):
    """Create a new project"""
    session = Session()
    try:
        # Check if client exists
        client = session.query(Client).filter_by(id=client_id).first()
        if not client:
            click.echo(f"❌ Client with ID {client_id} not found!")
            click.echo("💡 Use 'python cli.py client list' to see available clients")
            return
        
        # Create new project
        new_project = Project(
            name=name,
            client_id=client_id,
            hourly_rate=rate,
            description=description if description else None
        )
        
        session.add(new_project)
        session.commit()
        
        click.echo(f"✅ Project '{name}' created for {client.name}!")
        click.echo(f"💰 Hourly rate: ${rate:.2f}")
        click.echo("💡 Start logging time with 'python cli.py time log'")
        
    except Exception as e:
        session.rollback()
        click.echo(f"❌ Error creating project: {str(e)}")
    finally:
        session.close()

@project.command()
def list():
    """View all your projects"""
    session = Session()
    try:
        projects = session.query(Project).all()
        
        if not projects:
            click.echo("📭 No projects found. Create your first project with 'python cli.py project add'")
            return
        
        # Prepare data for table
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
        
    except Exception as e:
        click.echo(f"❌ Error fetching projects: {str(e)}")
    finally:
        session.close()

# ================================
# TIME TRACKING COMMANDS
# ================================

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
    session = Session()
    try:
        # Check if project exists
        project = session.query(Project).filter_by(id=project_id).first()
        if not project:
            click.echo(f"❌ Project with ID {project_id} not found!")
            click.echo("💡 Use 'python cli.py project list' to see available projects")
            return
        
        # Create new time entry
        new_entry = TimeEntry(
            project_id=project_id,
            hours_worked=hours,
            description=description,
            task_type=task_type if task_type else None
        )
        
        session.add(new_entry)
        session.commit()
        
        earnings = hours * project.hourly_rate
        
        click.echo(f"✅ Time logged successfully!")
        click.echo(f"📊 {hours} hours on '{project.name}'")
        click.echo(f"💰 You earned ${earnings:.2f}!")
        
    except Exception as e:
        session.rollback()
        click.echo(f"❌ Error logging time: {str(e)}")
    finally:
        session.close()

@time.command()
@click.option('--days', default=7, help='Number of days to show (default: 7)')
def recent(days):
    """View recent time entries"""
    session = Session()
    try:
        # Get time entries from the last N days
        cutoff_date = datetime.now() - timedelta(days=days)
        entries = session.query(TimeEntry).filter(
            TimeEntry.date >= cutoff_date
        ).order_by(TimeEntry.date.desc()).all()
        
        if not entries:
            click.echo(f"📭 No time entries found in the last {days} days")
            click.echo("💡 Log your first time entry with 'python cli.py time log'")
            return
        
        # Prepare data for table
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
        
    except Exception as e:
        click.echo(f"❌ Error fetching time entries: {str(e)}")
    finally:
        session.close()

# ================================
# REPORTS AND ANALYTICS
# ================================

@cli.command()
def summary():
    """📈 View business summary"""
    session = Session()
    try:
        # Get all data
        clients = session.query(Client).all()
        projects = session.query(Project).all()
        time_entries = session.query(TimeEntry).all()
        
        # Calculate totals
        total_clients = len(clients)
        total_projects = len(projects)
        total_hours = sum(entry.hours_worked for entry in time_entries)
        total_earnings = sum(entry.get_earnings() for entry in time_entries)
        
        # This month's earnings
        now = datetime.now()
        month_start = datetime(now.year, now.month, 1)
        month_entries = session.query(TimeEntry).filter(
            TimeEntry.date >= month_start
        ).all()
        month_earnings = sum(entry.get_earnings() for entry in month_entries)
        month_hours = sum(entry.hours_worked for entry in month_entries)
        
        click.echo("\n" + "="*50)
        click.echo("📈 FREELANCE BUSINESS SUMMARY")
        click.echo("="*50)
        click.echo(f"👥 Total Clients: {total_clients}")
        click.echo(f"📁 Total Projects: {total_projects}")
        click.echo(f"⏰ Total Hours Worked: {total_hours:.1f}")
        click.echo(f"💰 Total Earnings: ${total_earnings:.2f}")
        click.echo("\n" + "-"*30)
        click.echo(f"📅 This Month ({now.strftime('%B %Y')}):")
        click.echo(f"⏰ Hours: {month_hours:.1f}")
        click.echo(f"💰 Earnings: ${month_earnings:.2f}")
        
        if total_hours > 0:
            avg_rate = total_earnings / total_hours
            click.echo(f"📊 Average Rate: ${avg_rate:.2f}/hour")
        
        click.echo("="*50)
        
    except Exception as e:
        click.echo(f"❌ Error generating summary: {str(e)}")
    finally:
        session.close()

# ================================
# MAIN ENTRY POINT
# ================================

if __name__ == '__main__':
    cli()