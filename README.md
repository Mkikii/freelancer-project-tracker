Freelancer Project & Time Tracker
A Python command-line application for freelancers to manage clients, projects, and time logs — with built-in earnings reporting.

Overview
The Freelancer Project & Time Tracker is a lightweight CLI tool designed to help freelancers manage their business operations. It enables users to:

Create and manage client profiles

Link projects to clients with custom rates

Log work hours with task descriptions

Generate earnings reports by client or project

Built with Click for the CLI and SQLAlchemy for ORM-based database interactions.

Prerequisites
Before installing, ensure you have:

Python 3.8 or higher

Pipenv for virtual environment and dependency management

Git (for cloning the repository)

Installation
Clone the repository

bash
git clone https://github.com/your-username/freelancer-tracker.git
cd freelancer-tracker
Set up a virtual environment and install dependencies

bash
pipenv install
pipenv shell
Initialize the database

bash
python -c "from lib.models import Base, engine; Base.metadata.create_all(engine)"
Seed with sample data (optional)

bash
python -c "from lib.seed import seed_database; seed_database()"
Usage
Run the CLI application:

bash
python main.py
Available Commands
Command	Description
add-client	Add a new client
list-clients	View all clients
add-project	Add a new project
list-projects	View all projects
add-time	Log time worked
list-time	View time entries
earnings-report	Generate earnings report
seed	Seed database with sample data
Project Structure
Code
freelancer-tracker/
├── lib/
│   ├── __init__.py
│   ├── models.py         # SQLAlchemy models
│   ├── crud.py           # DB operations
│   ├── helpers.py        # Utility functions
│   └── seed.py           # Sample data seeding
├── main.py               # CLI entry point
├── Pipfile               # Dependency management
├── Pipfile.lock
├── README.md
└── .gitignore
Database Schema
Clients
id, name, email, company, phone, hourly_rate, created_at

Projects
id, name, description, client_id, hourly_rate, status, deadline, created_at

TimeEntries
id, project_id, date_worked, hours, description, task_type, created_at

Documentation
For deeper understanding of the CLI structure and logic, refer to:

main.py — CLI command definitions

lib/models.py — SQLAlchemy database schema

lib/crud.py — Database operations

lib/helpers.py — Utility functions

Inline comments and docstrings throughout the codebase

Author
Maureen W Karimi Email: maureen.karimi@student.moringaschool.com GitHub: github.com/maureenkarimi

Contributing
Contributions are welcome and appreciated. To contribute:

Fork the repository

Create a new branch (git checkout -b feature-name)

Make your changes with clear, descriptive commit messages

Push to your fork and open a pull request

Please follow the existing code structure and include relevant documentation or comments. All contributions should maintain the project's clean setup and beginner-friendly standards.

License
This project is licensed under the MIT License.
