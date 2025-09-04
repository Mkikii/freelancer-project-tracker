# Freelancer Project Tracker

A command-line application for freelancers to manage clients, projects, time tracking, and earnings reports.

---

## How It Works

### Database Structure (`models.py`)

- **Client**: Stores client information (name, email, phone, company, hourly rate).
- **Project**: Linked to clients, with custom rates and deadlines.
- **TimeEntry**: Logs hours worked per project and calculates earnings.

The database is created automatically using SQLAlchemy ORM when the application runs. No manual migrations are required.

---

## Features

- Add, view, and manage clients.
- Track projects with custom rates and deadlines.
- Log work hours with automatic earnings calculation.
- Generate time and earnings reports by client and project.

---

## Prerequisites

- Python 3.10+
- Pipenv installed

---

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

---

## Getting Started

Run the application using `cli.py`. No need to run `main.py`.

---

## Project Structure

```
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
```

---

## CLI Commands (`cli.py`)

- `add-client`: Add a new client.
- `list-clients`: View all clients.
- `add-project`: Add a project for a specific client.
- `list-projects`: View all projects.
- `log-time-entry`: Log work hours on a project.
- `time-report`: Generate a time worked report.
- `earnings-report`: Generate an earnings report.

---

## Usage Examples

```bash
python lib/cli.py add-client
python lib/cli.py list-clients
python lib/cli.py add-project
python lib/cli.py log-time-entry
python lib/cli.py time-report
python lib/cli.py earnings-report
```

---

## Data Structures

This project makes use of:

- **Lists**: For displaying multiple clients, projects, and time entries.
- **Dictionaries**: For aggregating earnings and hours per client.
- **Tuples**: Used implicitly in query results and CLI formatting.

---

## Documentation

More detailed documentation, including a full list of command options and internal logic, will be added soon.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed updates.

---

## Author

my name is Maureen K

---

## License

MIT License
