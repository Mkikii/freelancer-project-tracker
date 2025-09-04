Freelancer Project & Time Tracker
A comprehensive command-line application for freelancers to manage clients, projects, and track time worked with earnings reporting capabilities.

Description
Freelancer Project & Time Tracker is a CLI application designed to help freelancers manage their business operations efficiently. The application provides functionality for tracking clients, managing projects, logging work hours, and generating earnings reports. Built with Python, SQLAlchemy ORM, and Click for the CLI interface, it demonstrates modern database management and command-line application development.

Features
Client Management: Create, view, and manage client profiles with contact information and hourly rates

Project Management: Create projects linked to specific clients with custom rates and statuses

Time Tracking: Log hours worked on projects with descriptions and task types

Earnings Reporting: Generate comprehensive earnings reports by client and project

CRUD Operations: Full Create, Read, Update, and Delete functionality for all entities

Data Validation: Comprehensive input validation with proper error handling

SQLite Database: Lightweight and efficient database storage

User-Friendly CLI: Intuitive command-line interface with clear prompts

Technologies Used
Python 3.8+: Core programming language

SQLAlchemy: Object-Relational Mapping for database operations

Click: Python package for creating command-line interfaces

SQLite: Lightweight database engine for data persistence

DateTime: Python module for handling date and time operations

Project Structure
text
freelancer-tracker/
├── lib/
│   ├── __init__.py
│   ├── models.py          # Database models and schema
│   ├── crud.py            # Database operations and CRUD functions
│   ├── helpers.py         # Utility functions and validations
│   └── seed.py            # Database seeding script
├── main.py                # Main CLI application entry point
├── Pipfile                # Pipenv dependency management
├── Pipfile.lock           # Locked dependencies
├── README.md              # Project documentation
└── .gitignore            # Git ignore rules
Installation and Setup
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Installation Process
Navigate to the project directory:

bash
cd freelancer-tracker
Set up virtual environment using Pipenv:

bash
pipenv install
pipenv shell
Initialize the database:

bash
python -c "from lib.models import Base, engine; Base.metadata.create_all(engine); print('Database created successfully!')"
Seed the database with sample data:

bash
python -c "from lib.seed import seed_database; seed_database()"
Run the application:

bash
python main.py
How to Use
Starting the Application
Run the main script to start the interactive CLI:

bash
python main.py
Available Commands
add-client: Add a new client

list-clients: List all clients

add-project: Add a new project

list-projects: List all projects

add-time: Log time worked on a project

list-time: List time entries

earnings-report: Generate earnings report

seed: Seed database with sample data

Examples
Add a new client:

bash
python main.py add-client
Add a new project:

bash
python main.py add-project
Log time worked:

bash
python main.py add-time
Generate earnings report:

bash
python main.py earnings-report
Database Schema
Key Tables
Clients Table

id, name, email, company, phone, hourly_rate, created_at

Relationships with Projects

Projects Table

id, name, description, client_id, hourly_rate, status, deadline, created_at

Relationships with Clients and TimeEntries

TimeEntries Table

id, project_id, date_worked, hours, description, task_type, created_at

Relationships with Projects

API Reference (CRUD Functions)
Client Operations (lib/crud.py)
create_client() - Create new client profile

get_all_clients() - Retrieve all clients

get_client_by_id() - Get client by ID

Project Operations
create_project() - Create new project

get_all_projects() - Retrieve all projects

get_projects_by_client() - Get projects by client ID

Time Entry Operations
log_time() - Create new time entry

get_time_entries() - Retrieve time entries

get_earnings_report() - Generate earnings report

Development
Adding New Features
Update models in lib/models.py

Add CRUD operations in lib/crud.py

Update CLI interface in main.py

Test thoroughly

Common Issues and Solutions
Module Import Issues

python
# Correct import syntax
from lib import crud, models
# or
from lib.crud import create_client
Database Issues

bash
# Recreate database
rm freelancer.db
python -c "from lib.models import Base, engine; Base.metadata.create_all(engine)"
python -c "from lib.seed import seed_database; seed_database()"
Virtual Environment Issues

bash
# Recreate virtual environment
pipenv --rm
pipenv install
pipenv shell
Support and Contact Details
If you have any questions or need assistance, please contact:

Maureen W Karimi

maureen.karimi@student.moringaschool.com

License
This project is licensed under the MIT License.

If you find this project useful, please give it a star on GitHub!

