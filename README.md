Freelancer Project & Time Tracker
A comprehensive command-line application for freelancers to manage clients, projects, and track time with earnings reports.

Description
The Freelancer Project & Time Tracker is a CLI application designed to help freelancers manage their business operations. It provides functionality for tracking clients, managing projects, logging work hours, and generating earnings reports. The application is built with Python, SQLAlchemy ORM, and the Click library.

Features
Client Management: Create, view, and manage client profiles with contact information and hourly rates.

Project Management: Create projects linked to specific clients with custom rates and statuses.

Time Tracking: Log hours worked on projects with descriptions and task types.

Earnings Reporting: Generate comprehensive earnings reports by client and project.

CRUD Operations: Full Create, Read, Update, and Delete functionality for all entities.

Data Validation: Comprehensive input validation with proper error handling.

SQLite Database: A lightweight database for data storage.

User-Friendly CLI: An intuitive command-line interface with clear prompts.

Technologies Used
Python 3.8+: The core programming language.

SQLAlchemy: An Object-Relational Mapper (ORM) for database operations.

Click: A Python package for creating command-line interfaces.

SQLite: A lightweight database engine for data persistence.

DateTime: A Python module for handling date and time operations.

Project Structure
Plaintext

freelancer-tracker/
├── lib/
│   ├── __init__.py
│   ├── models.py       # Database models and schema
│   ├── crud.py         # Database operations and CRUD functions
│   ├── helpers.py      # Utility functions and validations
│   └── seed.py         # Database seeding script
├── main.py             # Main CLI application entry point
├── Pipfile             # Pipenv dependency management
├── Pipfile.lock        # Locked dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
Installation and Setup
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Installation Process
Navigate to the project directory:

Bash

cd freelancer-tracker
Set up the virtual environment using Pipenv:

Bash

pipenv install
pipenv shell
Initialize the database:

Bash

python -c "from lib.models import Base, engine; Base.metadata.create_all(engine); print('Database created successfully!')"
Seed the database with sample data:

Bash

python -c "from lib.seed import seed_database; seed_database()"
How to Use
Starting the Application
Run the main script to start the interactive CLI:

Bash

python main.py
Available Commands
add-client: Add a new client.

list-clients: List all clients.

add-project: Add a new project.

list-projects: List all projects.

add-time: Log time worked on a project.

list-time: List time entries.

earnings-report: Generate an earnings report.

seed: Seed the database with sample data.

Database Schema
Key Tables
Clients Table

Columns: id, name, email, company, phone, hourly_rate, created_at

Relationships: Linked to Projects.

Projects Table

Columns: id, name, description, client_id, hourly_rate, status, deadline, created_at

Relationships: Linked to Clients and TimeEntries.

TimeEntries Table

Columns: id, project_id, date_worked, hours, description, task_type, created_at

Relationships: Linked to Projects.

API Reference (CRUD Functions)
These functions are located in lib/crud.py and handle database operations.

Client Operations
create_client(): Create a new client profile.

get_all_clients(): Retrieve all clients.

get_client_by_id(): Get a client by their ID.

Project Operations
create_project(): Create a new project.

get_all_projects(): Retrieve all projects.

get_projects_by_client(): Get projects by client ID.

Time Entry Operations
log_time(): Create a new time entry.

get_time_entries(): Retrieve time entries.

get_earnings_report(): Generate an earnings report.

Development
Adding New Features
To add new functionality, follow these steps:

Update the database models in lib/models.py.

Add CRUD operations in lib/crud.py.

Update the CLI interface in main.py.

Test your new feature thoroughly.

Common Issues and Solutions
Module Import Issues: Ensure you're using the correct import syntax, like from lib import crud, models or from lib.crud import create_client.

Database Issues: To reset the database, delete the existing file and recreate it:

Bash

rm freelancer.db
python -c "from lib.models import Base, engine; Base.metadata.create_all(engine)"
python -c "from lib.seed import seed_database; seed_database()"
Virtual Environment Issues: If your virtual environment is corrupted, you can recreate it:

Bash

pipenv --rm
pipenv install
pipenv shell
Support and Contact
If you have any questions or need assistance, please contact:

Maureen W Karimi
Email: maureen.karimi@student.moringaschool.com

License
This project is licensed under the MIT License.
