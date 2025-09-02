Freelancer Tracker CLI - A command-line application that helps freelancers manage their business by tracking clients, projects, time worked, and earnings.

How It Works:
Database Structure (models.py):

Client table: Stores client info (name, email, hourly rate)

Project table: Stores projects linked to clients (with custom rates & deadlines)

TimeEntry table: Tracks hours worked on each project

CLI Commands (cli.py):

add-client: Register new clients

add-project: Create projects for clients

log-time: Record work hours

list-clients/list-projects: View data

time-report/earnings-report: Generate business insights

Helpers (helpers.py):

Input validation (email format)

Data structure handling (lists/dictionaries)

Database session management

Key Features:
✅ Client management with hourly rates

✅ Project tracking with custom pricing

✅ Time tracking and earnings calculations

✅ Business reports and analytics

✅ SQLite database storage

Installation & Update:
bash

# Install click (already installed via Pipfile)

pipenv install click==8.1.3

# Update README.md

cat > README.md << 'EOF'

# Freelancer Tracker

A command-line application for freelancers to manage clients, projects, time tracking, and earnings reports.

## Features

- Client management with hourly rates
- Project tracking with custom pricing
- Time entry logging
- Earnings reports by client and time period
- Business analytics and insights

## Installation

```bash
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
Author
Maureen K - Freelancer Business Management System

License
MIT License
```
