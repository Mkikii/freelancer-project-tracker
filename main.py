import click
from crud import (
    add_client, get_all_clients, get_client_by_id, update_client, delete_client,
    add_project, get_all_projects, get_project_by_id, update_project_status, delete_project,
    add_time_entry, get_recent_time_entries, get_all_time_entries, update_time_entry, delete_time_entry,
    add_category, get_all_categories, get_category_by_id,
    get_business_summary, get_client_earnings
)
from tabulate import tabulate
from models import init_db
from seed import seed_database
from debug import debug_database

def get_valid_int_input(prompt_text, default_value=None):
    """Get valid integer input from user with error handling"""
    while True:
        try:
            if default_value is not None:
                value = click.prompt(prompt_text, default=default_value, type=int)
            else:
                value = click.prompt(prompt_text, type=int)
            return value
        except click.BadParameter:
            click.secho("❌ Please enter a valid number.", fg='red')

def show_welcome():
    """Display welcome message"""
    click.secho("\n" + "="*60, fg='blue')
    click.secho("💼 FREELANCER PROJECT & TIME TRACKER", fg='blue', bold=True)
    click.secho("Created by: Maureen W Karimi", fg='cyan')
    click.secho("Moringa School - Phase 3 Python CLI Project", fg='cyan')
    click.secho("="*60, fg='blue')

def show_main_menu():
    """Display main menu options"""
    click.secho("\n📋 MAIN MENU", fg='yellow', bold=True)
    click.secho("1. 👥 Client Management", fg='green')
    click.secho("2. 📁 Project Management", fg='green')
    click.secho("3. ⏰ Time Tracking", fg='green')
    click.secho("4. 🏷️ Category Management", fg='green')
    click.secho("5. 📊 Reports & Analytics", fg='green')
    click.secho("6. 🛠️ Database Tools", fg='magenta')
    click.secho("7. ❌ Exit Application", fg='red')

def client_menu():
    """Handle client management"""
    while True:
        click.secho("\n👥 CLIENT MANAGEMENT", fg='blue', bold=True)
        click.secho("1. Add New Client", fg='yellow')
        click.secho("2. View All Clients", fg='yellow')
        click.secho("3. View Client Details", fg='yellow')
        click.secho("4. Update Client", fg='yellow')
        click.secho("5. Delete Client", fg='yellow')
        click.secho("6. Back to Main Menu", fg='red')
        
        choice = get_valid_int_input("Select option")
        
        if choice == 1:
            click.secho("\n➕ Adding New Client...", fg='yellow')
            name = click.prompt("Client name")
            email = click.prompt("Email address")
            company = click.prompt("Company (optional)", default="")
            phone = click.prompt("Phone (optional)", default="")
            
            success, message = add_client(
                name, email, 
                company if company else None, 
                phone if phone else None
            )
            
            if success:
                click.secho(f"✅ {message}", fg='green')
            else:
                click.secho(f"❌ {message}", fg='red')
                
        elif choice == 2:
            click.secho("\n👥 YOUR CLIENTS:", fg='blue')
            clients = get_all_clients()
            
            if not clients:
                click.secho("📭 No clients found.", fg='yellow')
            else:
                table_data = []
                for client in clients:
                    total_earnings = client.get_total_earnings()
                    projects_count = len(client.projects)
                    
                    table_data.append([
                        client.id,
                        client.name,
                        client.company or "N/A",
                        client.email,
                        projects_count,
                        f"${total_earnings:.2f}"
                    ])
                
                headers = ["ID", "Name", "Company", "Email", "Projects", "Total Earned"]
                click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
                
        elif choice == 3:
            client_id = get_valid_int_input("Enter Client ID")
            client = get_client_by_id(client_id)
            
            if not client:
                click.secho(f"❌ Client with ID {client_id} not found!", fg='red')
            else:
                click.secho(f"\n👥 CLIENT DETAILS: {client.name}", fg='blue')
                click.secho(f"📧 Email: {client.email}")
                click.secho(f"🏢 Company: {client.company or 'N/A'}")
                click.secho(f"📞 Phone: {client.phone or 'N/A'}")
                click.secho(f"📅 Created: {client.created_at.strftime('%Y-%m-%d')}")
                
                if client.notes:
                    click.secho(f"📝 Notes: {client.notes}")
                
                if client.projects:
                    click.secho(f"\n📁 PROJECTS ({len(client.projects)}):", fg='blue')
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
                click.secho(f"\n💰 TOTAL EARNED FROM CLIENT: ${total_earnings:.2f}", fg='green')
                
        elif choice == 4:
            client_id = get_valid_int_input("Enter Client ID to update")
            client = get_client_by_id(client_id)
            
            if not client:
                click.secho(f"❌ Client with ID {client_id} not found!", fg='red')
            else:
                click.secho(f"\n✏️ Updating Client: {client.name}", fg='yellow')
                name = click.prompt("New name (or press Enter to keep current)", default=client.name)
                email = click.prompt("New email (or press Enter to keep current)", default=client.email)
                company = click.prompt("New company (or press Enter to keep current)", default=client.company or "")
                phone = click.prompt("New phone (or press Enter to keep current)", default=client.phone or "")
                
                update_data = {}
                if name != client.name:
                    update_data['name'] = name
                if email != client.email:
                    update_data['email'] = email
                if company != (client.company or ""):
                    update_data['company'] = company if company else None
                if phone != (client.phone or ""):
                    update_data['phone'] = phone if phone else None
                
                if update_data:
                    success, message = update_client(client_id, **update_data)
                    if success:
                        click.secho(f"✅ {message}", fg='green')
                    else:
                        click.secho(f"❌ {message}", fg='red')
                else:
                    click.secho("ℹ️ No changes made.", fg='yellow')
                    
        elif choice == 5:
            client_id = get_valid_int_input("Enter Client ID to delete")
            client = get_client_by_id(client_id)
            
            if not client:
                click.secho(f"❌ Client with ID {client_id} not found!", fg='red')
            else:
                if click.confirm(f"⚠️ Are you sure you want to delete client '{client.name}'? This will also delete all their projects and time entries."):
                    success, message = delete_client(client_id)
                    if success:
                        click.secho(f"✅ {message}", fg='green')
                    else:
                        click.secho(f"❌ {message}", fg='red')
                else:
                    click.secho("Deletion cancelled.", fg='yellow')
                    
        elif choice == 6:
            break
        else:
            click.secho("❌ Invalid option. Please try again.", fg='red')

def project_menu():
    """Handle project management"""
    while True:
        click.secho("\n📁 PROJECT MANAGEMENT", fg='blue', bold=True)
        click.secho("1. Add New Project", fg='yellow')
        click.secho("2. View All Projects", fg='yellow')
        click.secho("3. View Project Details", fg='yellow')
        click.secho("4. Update Project Status", fg='yellow')
        click.secho("5. Delete Project", fg='yellow')
        click.secho("6. Back to Main Menu", fg='red')
        
        choice = get_valid_int_input("Select option")
        
        if choice == 1:
            click.secho("\n➕ Creating New Project...", fg='yellow')
            
            clients = get_all_clients()
            if not clients:
                click.secho("❌ No clients found! Add a client first.", fg='red')
                continue
                
            click.secho("\nAvailable Clients:", fg='cyan')
            for client in clients:
                click.secho(f"  {client.id}. {client.name} ({client.company or 'No company'})")
            
            name = click.prompt("Project name")
            client_id = get_valid_int_input("Client ID")
            
            client = get_client_by_id(client_id)
            if not client:
                click.secho(f"❌ Client with ID {client_id} not found!", fg='red')
                click.secho("Available Clients:", fg='cyan')
                for client in clients:
                    click.secho(f"  {client.id}. {client.name} ({client.company or 'No company'})")
                continue
            
            rate = click.prompt("Hourly rate ($)", type=float, default=25.0)
            description = click.prompt("Description (optional)", default="")
            
            categories = get_all_categories()
            if categories:
                click.secho("\nAvailable Categories:", fg='cyan')
                for category in categories:
                    click.secho(f"  {category.id}. {category.name}")
                category_id = click.prompt("Category ID (optional, press Enter to skip)", default="")
                try:
                    category_id = int(category_id) if category_id else None
                except ValueError:
                    category_id = None
            else:
                category_id = None
            
            success, message = add_project(
                name, client_id, rate,
                description if description else None,
                category_id
            )
            
            if success:
                click.secho(f"✅ {message}", fg='green')
            else:
                click.secho(f"❌ {message}", fg='red')
                
        elif choice == 2:
            click.secho("\n📁 YOUR PROJECTS:", fg='blue')
            projects = get_all_projects()
            
            if not projects:
                click.secho("📭 No projects found.", fg='yellow')
            else:
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
                click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
                
        elif choice == 3:
            project_id = get_valid_int_input("Enter Project ID")
            project = get_project_by_id(project_id)
            
            if not project:
                click.secho(f"❌ Project with ID {project_id} not found!", fg='red')
            else:
                click.secho(f"\n📁 PROJECT DETAILS: {project.name}", fg='blue')
                click.secho(f"👥 Client: {project.client.name}")
                click.secho(f"💰 Hourly Rate: ${project.hourly_rate:.2f}")
                click.secho(f"📊 Status: {project.status.upper()}")
                click.secho(f"📅 Created: {project.created_at.strftime('%Y-%m-%d')}")
                
                if project.description:
                    click.secho(f"📝 Description: {project.description}")
                
                if project.deadline:
                    click.secho(f"⏰ Deadline: {project.deadline.strftime('%Y-%m-%d')}")
                
                if project.category:
                    click.secho(f"🏷️ Category: {project.category.name}")
                
                if project.time_entries:
                    click.secho(f"\n⏰ TIME ENTRIES ({len(project.time_entries)}):", fg='blue')
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
                click.secho(f"\n📊 TOTALS: {total_hours:.2f} hours | 💰 ${total_earnings:.2f}", fg='green')
                
        elif choice == 4:
            click.secho("\n🔄 Update Project Status...", fg='yellow')
            projects = get_all_projects()
            
            if not projects:
                click.secho("❌ No projects found!", fg='red')
                continue
                
            project_id = get_valid_int_input("Project ID")
            new_status = click.prompt("New status", 
                                    type=click.Choice(['active', 'completed', 'paused']))
            
            success, message = update_project_status(project_id, new_status)
            
            if success:
                click.secho(f"✅ {message}", fg='green')
            else:
                click.secho(f"❌ {message}", fg='red')
                
        elif choice == 5:
            project_id = get_valid_int_input("Enter Project ID to delete")
            project = get_project_by_id(project_id)
            
            if not project:
                click.secho(f"❌ Project with ID {project_id} not found!", fg='red')
            else:
                if click.confirm(f"⚠️ Are you sure you want to delete project '{project.name}'? This will also delete all its time entries."):
                    success, message = delete_project(project_id)
                    if success:
                        click.secho(f"✅ {message}", fg='green')
                    else:
                        click.secho(f"❌ {message}", fg='red')
                else:
                    click.secho("Deletion cancelled.", fg='yellow')
                    
        elif choice == 6:
            break
        else:
            click.secho("❌ Invalid option. Please try again.", fg='red')

def time_tracking_menu():
    """Handle time tracking"""
    while True:
        click.secho("\n⏰ TIME TRACKING", fg='blue', bold=True)
        click.secho("1. Log Time Entry", fg='yellow')
        click.secho("2. View Recent Time Entries", fg='yellow')
        click.secho("3. Back to Main Menu", fg='red')
        
        choice = get_valid_int_input("Select option")
        
        if choice == 1:
            click.secho("\n⏰ Logging Work Time...", fg='yellow')
            
            projects = get_all_projects()
            if not projects:
                click.secho("❌ No projects found! Create a project first.", fg='red')
                continue
                
            click.secho("\nAvailable Projects:", fg='cyan')
            for project in projects:
                click.secho(f"  {project.id}. {project.name} (${project.hourly_rate:.2f}/hr)")
            
            project_id = get_valid_int_input("Project ID")
            
            project = get_project_by_id(project_id)
            if not project:
                click.secho(f"❌ Project with ID {project_id} not found!", fg='red')
                click.secho("Available Projects:", fg='cyan')
                for project in projects:
                    click.secho(f"  {project.id}. {project.name} (${project.hourly_rate:.2f}/hr)")
                continue
            
            hours = click.prompt("Hours worked", type=float)
            description = click.prompt("What did you work on?")
            task_type = click.prompt("Task type (optional)", default="")
            
            success, message = add_time_entry(
                project_id, hours, description,
                task_type if task_type else None
            )
            
            if success:
                click.secho(f"✅ {message}", fg='green')
            else:
                click.secho(f"❌ {message}", fg='red')
                
        elif choice == 2:
            days = get_valid_int_input("Show entries from last X days", 7)
            
            click.secho(f"\n⏰ TIME ENTRIES (Last {days} days):", fg='blue')
            entries = get_recent_time_entries(days)
            
            if not entries:
                click.secho("📭 No time entries found.", fg='yellow')
            else:
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
                        entry.description[:40] + "..." if len(entry.description) > 40 else entry.description,
                        f"${earnings:.2f}"
                    ])
                
                headers = ["Date", "Project", "Hours", "Description", "Earned"]
                click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
                click.secho(f"\n📊 TOTALS: {total_hours:.1f} hours | 💰 ${total_earnings:.2f}", fg='green')
                
        elif choice == 3:
            break
        else:
            click.secho("❌ Invalid option. Please try again.", fg='red')

def category_menu():
    """Handle category management"""
    while True:
        click.secho("\n🏷️ CATEGORY MANAGEMENT", fg='blue', bold=True)
        click.secho("1. Add New Category", fg='yellow')
        click.secho("2. View All Categories", fg='yellow')
        click.secho("3. Back to Main Menu", fg='red')
        
        choice = get_valid_int_input("Select option")
        
        if choice == 1:
            click.secho("\n➕ Adding New Category...", fg='yellow')
            name = click.prompt("Category name")
            description = click.prompt("Description (optional)", default="")
            color = click.prompt("Color code (optional, e.g., #FF5733)", default="")
            
            success, message = add_category(
                name,
                description if description else None,
                color if color else None
            )
            
            if success:
                click.secho(f"✅ {message}", fg='green')
            else:
                click.secho(f"❌ {message}", fg='red')
                
        elif choice == 2:
            click.secho("\n🏷️ CATEGORIES:", fg='blue')
            categories = get_all_categories()
            
            if not categories:
                click.secho("📭 No categories found.", fg='yellow')
            else:
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
                click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
                
        elif choice == 3:
            break
        else:
            click.secho("❌ Invalid option. Please try again.", fg='red')

def reports_menu():
    """Handle reports and analytics"""
    while True:
        click.secho("\n📊 REPORTS & ANALYTICS", fg='blue', bold=True)
        click.secho("1. Business Summary", fg='yellow')
        click.secho("2. Generate Detailed Report", fg='yellow')
        click.secho("3. Back to Main Menu", fg='red')
        
        choice = get_valid_int_input("Select option")
        
        if choice == 1:
            summary = get_business_summary()
            
            if not summary:
                click.secho("❌ Error generating business summary!", fg='red')
                continue
                
            click.secho("\n" + "="*50, fg='blue')
            click.secho("📈 FREELANCE BUSINESS SUMMARY", fg='blue', bold=True)
            click.secho("="*50, fg='blue')
            click.secho(f"👥 Total Clients: {summary['total_clients']}")
            click.secho(f"📁 Total Projects: {summary['total_projects']}")
            click.secho(f"⏰ Total Hours Worked: {summary['total_hours']:.1f}")
            click.secho(f"💰 Total Earnings: ${summary['total_earnings']:.2f}")
            click.secho("\n" + "-"*30, fg='blue')
            
            from datetime import datetime
            now = datetime.now()
            click.secho(f"📅 This Month ({now.strftime('%B %Y')}):", fg='blue')
            click.secho(f"⏰ Hours: {summary['month_hours']:.1f}")
            click.secho(f"💰 Earnings: ${summary['month_earnings']:.2f}")
            
            if summary['total_hours'] > 0:
                click.secho(f"📊 Average Rate: ${summary['avg_rate']:.2f}/hour")
            
            click.secho("="*50, fg='blue')
                
        elif choice == 2:
            days = get_valid_int_input("Generate report for last X days", 30)
            
            click.secho(f"\n📊 BUSINESS REPORT (Last {days} days)", fg='blue', bold=True)
            click.secho("="*60, fg='blue')
            
            from datetime import datetime, timedelta
            from models import get_session, TimeEntry
            
            cutoff_date = datetime.now() - timedelta(days=days)
            session = get_session()
            
            try:
                entries = session.query(TimeEntry).filter(
                    TimeEntry.date >= cutoff_date
                ).order_by(TimeEntry.date.desc()).all()
                
                if not entries:
                    click.secho("No time entries found for this period.", fg='yellow')
                    continue
                
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
                
                click.secho(f"📅 Period: {cutoff_date.strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}")
                click.secho(f"⏰ Total Hours: {total_hours:.2f}")
                click.secho(f"💰 Total Earnings: ${total_earnings:.2f}")
                click.secho("\n" + "-"*60, fg='blue')
                
                if projects:
                    click.secho("📁 PROJECT BREAKDOWN:", fg='blue')
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
                
                click.secho("\n📅 DAILY BREAKDOWN:", fg='blue')
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
                click.secho(f"❌ Error generating report: {str(e)}", fg='red')
            finally:
                session.close()
                
        elif choice == 3:
            break
        else:
            click.secho("❌ Invalid option. Please try again.", fg='red')

def database_tools_menu():
    """Handle database tools"""
    while True:
        click.secho("\n🛠️ DATABASE TOOLS", fg='blue', bold=True)
        click.secho("1. Seed Database with Sample Data", fg='yellow')
        click.secho("2. Debug Database", fg='yellow')
        click.secho("3. Back to Main Menu", fg='red')
        
        choice = get_valid_int_input("Select option")
        
        if choice == 1:
            if click.confirm("⚠️ This will delete all existing data and replace it with sample data. Are you sure?"):
                seed_database()
            else:
                click.secho("Seeding cancelled.", fg='yellow')
                
        elif choice == 2:
            debug_database()
                
        elif choice == 3:
            break
        else:
            click.secho("❌ Invalid option. Please try again.", fg='red')

def main():
    """Main application entry point"""
    init_db()
    
    while True:
        show_welcome()
        show_main_menu()
        
        try:
            choice = get_valid_int_input("Select option")
            
            if choice == 1:
                client_menu()
            elif choice == 2:
                project_menu()
            elif choice == 3:
                time_tracking_menu()
            elif choice == 4:
                category_menu()
            elif choice == 5:
                reports_menu()
            elif choice == 6:
                database_tools_menu()
            elif choice == 7:
                click.secho("👋 Thank you for using Freelancer Tracker! Goodbye!", fg='green')
                break
            else:
                click.secho("❌ Invalid option. Please try again.", fg='red')
                
        except ValueError:
            click.secho("❌ Please enter a valid number.", fg='red')
        except KeyboardInterrupt:
            click.secho("\n👋 Goodbye!", fg='green')
            break
        except Exception as e:
            click.secho(f"❌ An error occurred: {str(e)}", fg='red')

if __name__ == "__main__":
    main()