from models import Client, Project, TimeEntry, Category, get_session
from crud import get_business_summary
from tabulate import tabulate

def debug_database():
    """Debug function to display database contents"""
    session = get_session()
    
    try:
        client_count = session.query(Client).count()
        project_count = session.query(Project).count()
        time_entry_count = session.query(TimeEntry).count()
        category_count = session.query(Category).count()
        
        print("=" * 60)
        print("🔧 DATABASE DEBUG INFORMATION")
        print("=" * 60)
        print(f"Clients: {client_count}")
        print(f"Projects: {project_count}")
        print(f"Time Entries: {time_entry_count}")
        print(f"Categories: {category_count}")
        print("-" * 60)
   
        summary = get_business_summary()
        if summary:
            print("📈 BUSINESS SUMMARY:")
            print(f"Total Hours: {summary['total_hours']:.2f}")
            print(f"Total Earnings: ${summary['total_earnings']:.2f}")
            print(f"This Month: {summary['month_hours']:.2f}h (${summary['month_earnings']:.2f})")
            print(f"Average Rate: ${summary['avg_rate']:.2f}/h")
        
        print("-" * 60)
        
        entries = session.query(TimeEntry).order_by(TimeEntry.date.desc()).limit(5).all()
        if entries:
            print("⏰ RECENT TIME ENTRIES:")
            table_data = []
            for entry in entries:
                table_data.append([
                    entry.date.strftime('%Y-%m-%d'),
                    entry.project.name[:20] + "..." if len(entry.project.name) > 20 else entry.project.name,
                    f"{entry.hours_worked:.2f}h",
                    f"${entry.get_earnings():.2f}"
                ])
            
            headers = ["Date", "Project", "Hours", "Earned"]
            print(tabulate(table_data, headers=headers, tablefmt="simple"))
        
        print("-" * 60)
       
        clients = session.query(Client).all()
        if clients:
            print("👥 TOP EARNING CLIENTS:")
            client_earnings = []
            for client in clients:
                earnings = client.get_total_earnings()
                if earnings > 0:
                    client_earnings.append((client.name, earnings))
            
            client_earnings.sort(key=lambda x: x[1], reverse=True)
            
            table_data = []
            for name, earnings in client_earnings[:5]:
                table_data.append([name, f"${earnings:.2f}"])
            
            headers = ["Client", "Total Earned"]
            print(tabulate(table_data, headers=headers, tablefmt="simple"))
        
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Error debugging database: {str(e)}")
    finally:
        session.close()

if __name__ == "__main__":
    debug_database()