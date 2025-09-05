# Freelancer Project & Time Tracker

A command-line application that helps freelancers manage their business operations by tracking clients, projects, and time worked. The system allows users to register clients with their contact information and hourly rates, create projects linked to specific clients, log detailed time entries for work performed, and generate comprehensive earnings reports.

---

## Prerequisites

* **Python 3.8** or higher
* **pipenv** (Python package manager)
* **Git**

---

## Installation and Setup

1.  **Clone the Repository**
    Navigate to your desired directory and clone the repository.
    ```bash
    git clone [https://github.com/Mkikii/freelancer-project-tracker](https://github.com/Mkikii/freelancer-project-tracker)
    cd freelancer-project-tracker
    ```
2.  **Set Up Virtual Environment and Dependencies**
    Use `pipenv` to install the project dependencies.
    ```bash
    pipenv install
    pipenv shell
    ```
3.  **Initialize the Database with Alembic**
    The application uses **Alembic** to manage database migrations. Run the following command to create the database and tables.
    ```bash
    alembic upgrade head
    ```
4.  **Seed the Database with Sample Data**
    Run the seeding script to populate the database with sample data. This is essential for testing the application's reporting features.
    ```bash
    python main.py seed
    ```

---

## How to Use

Run the main script to start the application and access its commands.

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
├── migrations/              # Alembic migration files
│   ├── versions/           # Migration scripts
│   ├── env.py              # Migration environment
│   └── script.py.mako      # Migration template
├── lib/
│   ├── __init__.py
│   ├── models.py           # SQLAlchemy database models (3+ tables)
│   ├── crud.py             # CRUD operations and database queries
│   ├── helpers.py          # Validation and utility functions
│   └── seed.py             # Database seeding with sample data
├── main.py                 # Main CLI application using Click
├── alembic.ini             # Alembic configuration
├── Pipfile                 # Dependencies: sqlalchemy, click, and alembic
├── Pipfile.lock
├── README.md
└── .gitignore

Author

Name: Maureen W Karimi

GitHub: Mkikii

License
This project is licensed under the MIT License.
