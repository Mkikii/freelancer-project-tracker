# 💼 Freelancer Project & Time Tracker

A comprehensive command-line application for freelancers to track clients, projects, and time worked. Built with Python, SQLAlchemy ORM, and Click for the Phase 3 project at Moringa School.

## ✨ Features

- **👥 Client Management**: Add, view, update, and delete clients
- **📁 Project Tracking**: Manage projects with hourly rates and statuses
- **⏰ Time Logging**: Track time worked on projects with descriptions
- **🏷️ Category System**: Organize projects by categories
- **📊 Reporting**: Generate business summaries and detailed reports
- **🛠️ Database Tools**: Seed with sample data and debug functionality

## 🛠️ Technologies Used

- Python 3.10+
- SQLAlchemy ORM
- Click for CLI interface
- Tabulate for formatted tables
- Faker for sample data generation

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd freelancer-tracker
pipenv install
pipenv shell
python cli.py
# Client management
python cli.py client add
python cli.py client list

# Project management
python cli.py project add
python cli.py project list

# Time tracking
python cli.py time log
python cli.py time recent

# Reports
python cli.py summary
python cli.py report

# Database tools
python cli.py seed
python cli.py debug
Interactive Menu Interface
Run the interactive menu:

bash
python main.py
🗃️ Database Schema
The application uses SQLite by default with the following tables:

clients: Store client information

projects: Track projects with hourly rates

time_entries: Record work sessions with hours and descriptions

categories: Organize projects by type

📊 Example Usage
Add a client:

text
python cli.py client add --name "Acme Corp" --email "contact@acme.com" --company "Acme Corporation" --phone "555-1234"
Create a project:

text
python cli.py project add --name "Website Redesign" --client-id 1 --rate 50.0 --description "Redesign of main website"
Log time:

text
python cli.py time log --project-id 1 --hours 3.5 --description "Designed homepage layout" --task-type "design"
Generate report:

text
python cli.py report --days 30
🧪 Testing
Seed the database with sample data:

bash
python cli.py seed
Debug database contents:

bash
python cli.py debug
📝 Project Structure
text
freelancer-tracker/
├── Pipfile               # Dependencies and virtual environment config
├── Pipfile.lock         # Locked dependencies
├── README.md            # This file
├── cli.py              # Command-line interface
├── crud.py             # Database operations (Create, Read, Update, Delete)
├── debug.py            # Database debugging utilities
├── main.py             # Interactive menu interface
├── models.py           # SQLAlchemy database models
└── seed.py             # Database seeding with sample data
👩‍💻 Author
Maureen W Karimi
Moringa School - Phase 3 Python CLI Project

📄 License
This project is created for educational purposes as part of the Moringa School curriculum.

text

## Setup Instructions

1. Create the project directory and navigate to it:
```bash
mkdir freelancer-tracker
cd freelancer-tracker
Create and activate a virtual environment with Pipenv:

bash
pipenv install
pipenv shell
Create all the files with the code provided above.

Initialize the database:

bash
python models.py
Seed the database with sample data:

bash
python seed.py
Run the application:

bash
# For the command-line interface
python cli.py --help

# For the interactive menu interface
python main.py
