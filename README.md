Freelancer Tracker CLI
A command-line application that helps freelancers manage clients, projects, time tracking, and earnings reports.

How It Works
Database Structure (models.py)

Client: Stores client info (name, email, phone, company, hourly rate)

Project: Linked to clients, with custom rates and deadlines

TimeEntry: Tracks hours worked per project

CLI Commands (cli.py)

add-client: Register new clients

list-clients: View all clients

add-project: Create projects for clients

log-time: Record work hours

earnings-report: Generate earnings summary

Helpers (helpers.py)

Input validation

Data structure handling

Database session management

Features
Client management with hourly rates

Project tracking with custom pricing

Time tracking and earnings calculations

Business reports and analytics

SQLite database storage

Prerequisites
Python 3.10+

Pipenv installed

Click (installed via Pipfile or manually with pipenv install click==8.1.3)

Installation
bash
git clone <your-repo>
cd freelancer-tracker
pipenv shell
pipenv install
Usage
bash
python lib/cli.py add-client --name "Client" --email "client@email.com" --rate 75.0
python lib/cli.py add-project --name "Project" --client-id 1 --rate 85.0
python lib/cli.py log-time --description "Work" --hours 5.0 --client-id 1 --project-id 1
python lib/cli.py earnings-report
python lib/cli.py list-clients
Documentation
More detailed documentation coming soon.

Contributing
Pull requests are welcome. For major changes, open an issue first to discuss the proposed updates.

Author
Maureen K

License
MIT License
