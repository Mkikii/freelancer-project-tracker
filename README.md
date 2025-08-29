Freelancer Project & Time Tracker
A comprehensive command-line application for freelancers to track clients, projects, and time worked. Built with Python, SQLAlchemy ORM, and Click for efficient management of freelance business operations.

Key Features
Client Management: Add, view, update, and delete client information with complete contact details and notes

Project Tracking: Manage projects with hourly rates, status tracking, deadlines, and categorization

Time Logging: Track work sessions with detailed descriptions, task types, and automatic earnings calculation

Category System: Organize projects by work types such as Web Development, Mobile Development, and UI/UX Design

Business Reporting: Generate comprehensive summaries and detailed reports of hours worked and earnings

Data Analytics: View business insights including total hours, earnings, and performance metrics

Sample Data Generation: Populate the database with realistic sample data for testing and demonstration

Technical Stack
This application is built with a robust Python backend stack, focusing on data persistence and command-line usability.

Python 3.8+: Core programming language

SQLAlchemy ORM: Database object-relational mapping for efficient data management

Click: Command-line interface framework for intuitive user interactions

Tabulate: Data formatting for clean, readable output tables

Faker: Sample data generation for testing and demonstration

Python-dotenv: Environment variable management for configuration

Project Architecture
The project follows a modular structure with clear separation of concerns:

text
freelancer-tracker/
├── cli.py # Command-line interface using Click
├── crud.py # Database operations (Create, Read, Update, Delete)
├── models.py # SQLAlchemy database models and schema
├── seed.py # Database seeding with sample data
├── debug.py # Debug utilities and database inspection
├── main.py # Interactive menu interface
├── requirements.txt # Project dependencies
├── Pipfile # Pipenv configuration
├── README.md # Project documentation
└── freelancer_tracker.db # SQLite database (generated)
Database Schema
The application uses SQLite with the following tables:

clients: Stores client information (name, email, company, phone, notes)

projects: Tracks project details (name, description, hourly rate, status, deadline)

time_entries: Records work sessions (hours, description, task type, date)

categories: Organizes projects by type (Web Development, Mobile Development, etc.)

Local Development Setup
To run the Freelancer Tracker on your local machine, follow these instructions.

Prerequisites
Ensure you have the following software installed on your system:

Python 3.8 or higher

Pipenv for virtual environment management

Step 1: Clone or Download the Project
Download the project files to your local machine and navigate to the project directory:

bash
cd freelancer-tracker
Step 2: Set Up Virtual Environment and Dependencies
Install dependencies using Pipenv:

bash
pipenv install
Activate the virtual environment:

bash
pipenv shell
Step 3: Initialize the Database
Create and initialize the SQLite database:

bash
python models.py
Step 4: Seed with Sample Data (Optional)
Populate the database with sample data for testing:

bash
python seed.py
Step 5: Run the Application
Use the command-line interface:

bash
python cli.py --help
Or use the interactive menu interface:

bash
python main.py
Usage
Command Line Interface
The application provides a comprehensive CLI with the following commands:

bash

# Client management

python cli.py client add --name "Client Name" --email "client@example.com"
python cli.py client list
python cli.py client view <ID>

# Project management

python cli.py project add --name "Project Name" --client-id 1 --rate 50.0
python cli.py project list

# Time tracking

python cli.py time log --project-id 1 --hours 3.5 --description "Work description"
python cli.py time recent --days 7

# Reports and analytics

python cli.py summary
python cli.py report --days 30

# Database utilities

python cli.py seed
python cli.py debug
Interactive Menu Interface
For users preferring a guided experience, run the interactive menu:

bash
python main.py
This provides a color-coded, menu-driven interface with all the same functionality.

Application Flow
Database Initialization: Start by running models.py to create the database schema

Client Management: Add clients before creating projects

Project Setup: Create projects associated with clients

Time Tracking: Log work hours against specific projects

Reporting: Generate business summaries and detailed reports

Maintenance: Use debug tools to monitor database health

Deployment
This application is designed to run locally and does not require web deployment. The SQLite database provides persistent storage, and all data remains on your local machine.

For production use, ensure regular backups of the freelancer_tracker.db file.

Environment Configuration
The application uses environment variables for configuration:

DATABASE_URL: Connection string for database (defaults to SQLite)

Other configuration options can be added to .env file

Contributing
Contributions are welcome. If you have suggestions for improvements, new features, or encounter any issues, please feel free to open an issue or submit a pull request.

License
This project is open-source and distributed under the MIT License.

Support
For questions or issues related to this application, please refer to the documentation above or check the GitHub repository for updates and community support.
