# Freelancer Project & Time Tracker

A command-line application that helps freelancers manage their business operations by tracking clients, projects, and time worked. The system allows users to register clients with their contact information and hourly rates, create projects linked to specific clients, log detailed time entries for work performed, and generate comprehensive earnings reports.

---

## Prerequisites

* **Python 3.8** or higher
* **pip** (Python package manager)
* **Git**

---

## Installation Instructions

1.  **Clone the Repository**
    Navigate to your desired directory and clone the repository.
    ```bash
    git clone <your-repository-url>
    cd freelancer-tracker
    ```
2.  **Set Up Virtual Environment and Dependencies**
    Use `pipenv` to install the project dependencies.
    ```bash
    pipenv install
    pipenv shell
    ```
3.  **Initialize the Database**
    The application uses SQLAlchemy ORM to automatically create the database and tables.
    ```bash
    python -c "from lib.models import Base, engine; Base.metadata.create_all(engine); print('Database created successfully!')"
    ```
4.  **Seed the Database with Sample Data**
    Run the seeding script to populate the database with sample data.
    ```bash
    python -c "from lib.seed import seed_database; seed_database()"
    ```

---

## Basic Usage Examples

Run the main script to start the application and access available commands.

```bash
python main.py
Available Commands
Add a New Client: python main.py add-client

List All Clients: python main.py list-clients

Add a New Project: python main.py add-project

List All Projects: python main.py list-projects

Log Time Worked: python main.py add-time

List Time Entries: python main.py list-time

Generate Earnings Report: python main.py earnings-report

Seed Database: python main.py seed

Project Structure
Plaintext

freelancer-tracker/
├── lib/
│   ├── __init__.py
│   ├── models.py          # SQLAlchemy database models
│   ├── crud.py            # CRUD operations and database queries
│   ├── helpers.py         # Validation and utility functions
│   └── seed.py            # Database seeding with sample data
├── main.py                # Main CLI application using Click
├── Pipfile                # Project dependencies
├── Pipfile.lock
├── README.md
└── .gitignore
Technical Features and Grading Criteria
This section outlines how the project meets the technical requirements for grading.

Configuration of Environment and Dependencies: Pipfile contains necessary dependencies (sqlalchemy and click). The project uses a clean import structure and proper module organization.

SQLAlchemy Schema Design: Uses SQLAlchemy ORM to create three related tables (clients, projects, time_entries). The database and tables are created automatically via SQLAlchemy, and data is converted for CLI use.

Use of Data Structures: The application uses lists for data collections, dictionaries for report data, and tuples for various function returns and data handling.

Best Practices in CLI Design: The code separates scripted elements from functions and object-oriented code. It includes comprehensive input validation, user-friendly prompts, and clear error messages.

Documentation: A comprehensive README.md file is included with installation, usage instructions, and a clear overview of the project's structure and features.

Author
Name: Maureen W Karimi

GitHub: Mkikii

License
This project is licensed under the MIT License.

