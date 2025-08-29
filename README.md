#  Freelancer Project & Time Tracker

A comprehensive command-line application for freelancers to track clients, projects, and time worked. Built with Python, SQLAlchemy ORM, and Click for the Phase 3 project at Moringa School.

## Features

- ** Client Management**: Add, view, update, and delete clients
- ** Project Tracking**: Manage projects with hourly rates and statuses
- ** Time Logging**: Track time worked on projects with descriptions
- ** Category System**: Organize projects by categories
- ** Reporting**: Generate business summaries and detailed reports
- ** Database Tools**: Seed with sample data and debug functionality
- ** Input Validation**: Comprehensive validation with user-friendly error messages
- ** Interactive Menus**: Color-coded interface with intuitive navigation

##  Technologies Used

- Python 3.10+
- SQLAlchemy ORM
- Click for CLI interface
- Tabulate for formatted tables
- Faker for sample data generation

##  Installation
1. **Clone or download the project files** to your local machine
2. 
3. **Navigate to the project directory**:
```bash
cd freelancer-tracker

Install dependencies using Pipenv:
bash
pipenv install

Activate the virtual environment:
bash
pipenv shell

Initialize the database:
bash
python models.py

Seed the database with sample data (optional):
bash
python seed.py
Usage
Command Line Interface (CLI)

Run the main application:
bash
python cli.py --help

Individual commands:
bash
# Client management
python cli.py client add
python cli.py client list
python cli.py client view <ID>

# Project management
python cli.py project add
python cli.py project list
python cli.py project view <ID>

# Time tracking
python cli.py time log
python cli.py time recent

# Reports
python cli.py summary
python cli.py report --days 30

# Database tools
python cli.py seed
python cli.py debug

Interactive Menu Interface

Run the interactive menu (recommended for new users):
bash
python main.py

**Database Schema
The application uses SQLite by default with the following tables:

clients: Store client information (name, email, company, phone, notes)

projects: Track projects with hourly rates, status, and deadlines

time_entries: Record work sessions with hours, descriptions, and task types

categories: Organize projects by type (Web Dev, Mobile, Design, etc.)

** Example Usage
Add a client:
bash
python cli.py client add --name "Acme Corp" --email "contact@acme.com" --company "Acme Corporation" --phone "555-1234"

Create a project (with input validation):
bash
# The application will validate all inputs and show helpful error messages
python cli.py project add --name "Website Redesign" --client-id 1 --rate 50.0 --description "Redesign of main website"

Log time:
bash
python cli.py time log --project-id 1 --hours 3.5 --description "Designed homepage layout" --task-type "design"

Generate report:
bash
python cli.py report --days 30

** Testing
Seed the database with sample data:
bash
python cli.py seed

Debug database contents:
bash
python cli.py debug

Test all functionality (recommended):
bash
python main.py

 ** Troubleshooting
Common Issues:

SQLAlchemy not found:
bash
pip install sqlalchemy==1.4.46

Database schema issues:
bash
rm freelancer_tracker.db
python models.py
python seed.py

** Click not installed:
bash
pip install click==8.1.3
Input validation errors - The application now provides clear error messages guiding you to enter valid data.

Project Structure
text
freelancer-tracker/
├── Pipfile               
├── Pipfile.lock         
├── README.md            
├── cli.py              
├── crud.py             
├── debug.py            
├── main.py             
├── models.py           
└── seed.py
            
 Author
 My name is Maureen K
Moringa School - Phase 3 Python CLI Project

📄 License
This project is created for educational purposes as part of the Moringa School curriculum.
