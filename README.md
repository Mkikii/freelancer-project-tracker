Freelancer Project & Time Tracker
A command-line application for freelancers to manage clients, projects, and track time with earnings reporting.

Description
The Freelancer Project & Time Tracker is a Python CLI application designed to help freelancers manage their business operations. It provides functionality for tracking clients, managing projects, logging work hours, and generating earnings reports. Built with SQLAlchemy ORM and Click for the command-line interface.

Features
Client Management: Create and manage client profiles with contact information and hourly rates

Project Management: Create projects linked to specific clients with custom rates

Time Tracking: Log hours worked on projects with descriptions and task types

Earnings Reporting: Generate comprehensive earnings reports by client and project

Data Validation: Input validation with proper error handling

SQLite Database: Lightweight database storage

Technologies Used
Python 3.8+

SQLAlchemy ORM

Click

SQLite

DateTime

Project Structure
freelancer-tracker/
├── lib/
│   ├── __init__.py
│   ├── models.py
│   ├── crud.py
│   ├── helpers.py
│   └── seed.py
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── .gitignore
Installation
Clone the repository

Navigate to the project directory

Install dependencies:
pipenv install
pipenv shell
Initialize the database:
python -c "from lib.models import Base, engine; Base.metadata.create_all(engine)"
python -c "from lib.models import Base, engine; Base.metadata.create_all(engine)"
Seed with sample data:
python -c "from lib.seed import seed_database; seed_database()"
Usage
Run the application:
python main.py
Available Commands
add-client: Add a new client

list-clients: List all clients

add-project: Add a new project

list-projects: List all projects

add-time: Log time worked

list-time: List time entries

earnings-report: Generate earnings report

seed: Seed database with sample data

Database Schema
Clients Table
id, name, email, company, phone, hourly_rate, created_at

Projects Table
id, name, description, client_id, hourly_rate, status, deadline, created_at

TimeEntries Table
id, project_id, date_worked, hours, description, task_type, created_at

Support
For questions or support, contact:

Maureen W Karimi

maureen.karimi@student.moringaschool.com

License
MIT License

