# Freelancer Project & Time Tracker

A command-line application built with Python for freelancers to manage clients, projects, and track time efficiently.

## Features
- Client management with contact information and rates
- Project creation and status tracking
- Time logging with detailed descriptions
- Earnings calculations and reporting
- Professional CLI interface with beautiful table outputs

## Technologies Used
- Python 3.8+
- SQLAlchemy (ORM)
- Click (CLI framework)
- SQLite (Database)
- Tabulate (Table formatting)

## Setup Instructions
1. Clone the repository
2. Create virtual environment: `python -m venv freelancer_env`
3. Activate environment: `source freelancer_env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run application: `python main.py --help`

## Usage Examples
```bash
# Add a client
python main.py client add

# Create a project
python main.py project add

# Log time
python main.py time log

# View earnings report
python main.py report earnings
