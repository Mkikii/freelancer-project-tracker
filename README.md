# Freelancer Project Tracker

A command-line application for freelancers to manage clients, projects, time tracking, and earnings reports.

## How It Works

### Database Structure (`models.py`)
- **Client**: Stores client information (name, email, phone, company, hourly rate).
- **Project**: Linked to clients, with custom rates and deadlines.
- **TimeEntry**: Logs hours worked per project and calculates earnings.

The database is created automatically using SQLAlchemy ORM when the application runs. No manual migrations are required.

Business logic and database operations are modularized in `lib/crud.py`, keeping the CLI clean and focused.

## Features
- Add, view, and manage clients.
- Track projects with custom rates and deadlines.
- Log work hours with automatic earnings calculation.
- Generate time and earnings reports by client and project.
  
## Prerequisites
- Python 3.10+
- Pipenv installed
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mkikii/freelancer-project-tracker.git
   cd freelancer-project-tracker
   ```

2. Activate the virtual environment and install dependencies:
   ```bash
   pipenv shell
   pipenv install
   ```

> **Note**: The database file (`.db`) is automatically created upon first use and is ignored by Git. Make sure `*.db` is listed in your `.gitignore`.

## Getting Started

Run the application using `cli.py`. 

## Project Structure

freelancer-project-tracker/
│
├── lib/
│   ├── cli.py          # CLI commands and user interaction
│   ├── crud.py         # Business logic and database operations
│   ├── models.py       # SQLAlchemy ORM models
│   ├── helpers.py      # Utility functions (e.g., email validation)
│   └── __init__.py
│
├── Pipfile
├── Pipfile.lock
├── .gitignore
└── README.md

## CLI Commands (`cli.py`)
- `add-client`: Add a new client.
- `list-clients`: View all clients.
- `add-project`: Add a project for a specific client.
- `list-projects`: View all projects.
- `log-time-entry`: Log work hours on a project.
- `time-report`: Generate a time worked report.
- `earnings-report`: Generate an earnings report.

## Usage Examples

bash
# Add a new client
python lib/cli.py add-client

# List all clients
python lib/cli.py list-clients

# Add a project for client with ID 1
python lib/cli.py add-project

# Log 5 hours of work on a project
python lib/cli.py log-time-entry

# Generate a time report
python lib/cli.py time-report --client-id 1

# Generate an earnings report
python lib/cli.py earnings-report --client-id 1 --start-date "2025-09-01" --end-date "2025-09-30"

## Data Structures

This project makes use of:
- **Lists**: For displaying multiple clients, projects, and time entries.
- **Dictionaries**: For aggregating earnings and hours per client.
- **Tuples**: Used implicitly in query results and CLI formatting.

## Documentation

More detailed documentation, including a full list of command options and internal logic, will be added soon.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed updates.

## Author

 my name is Maureen K

## License

MIT License
