Freelancer-Project-Tracker
A command-line application for freelancers to manage clients, projects, time tracking, and earnings reports.

How It Works
Database Structure (models.py)

Client: Stores client info (name, email, phone, company, hourly rate)

Project: Linked to clients, with custom rates and deadlines

TimeEntry: Logs hours worked per project and calculates earnings

CLI Commands (cli.py)

add-client: Add new client with details

list-clients: View all clients

add-project: Add project for client

list-projects: View all projects

log-time: Log work hours on project

time-report: Generate time worked report

earnings-report: Generate earnings report

Features
Client management (name, email, phone, company, hourly rate)

Project tracking with custom rates and deadlines

Time entry logging with earnings calculation

Time reports by client and project

Earnings reports by client and time period

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
python lib/cli.py add-client --name "Client" --email "client@email.com" --phone "0712345678" --company "Acme Inc." --rate 75.0
python lib/cli.py list-clients
python lib/cli.py add-project --name "Project" --client-id 1 --rate 85.0 --deadline "2025-09-30"
python lib/cli.py list-projects
python lib/cli.py log-time --description "Work session" --hours 5.0 --client-id 1 --project-id 1
python lib/cli.py time-report
python lib/cli.py earnings-report
Documentation
More detailed documentation will be added soon.

Contributing
Pull requests are welcome. For major changes, open an issue first to discuss the proposed updates.

Author
My name is My Name Maureen K

License
MIT License
