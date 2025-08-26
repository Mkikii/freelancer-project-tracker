# 💼 Freelancer Project & Time Tracker

**Created by: Maureen W Karimi**  
**Phase 3 Python CLI Project - Moringa School**

A simple command-line application that helps me manage my freelance business by tracking clients, projects, and time worked. Built with Python, SQLAlchemy ORM, and Click CLI framework.

## 🎯 Project Purpose

As a student learning to freelance, I needed a simple tool to:
- Keep track of my clients and their contact information
- Manage multiple projects with different rates
- Log time I spend working on each project
- Generate reports to see how much I'm earning

## ✨ Features

### 👥 Client Management
- Add new clients with contact details and hourly rates
- View all clients with earnings summary
- Track which clients are most profitable

### 🚀 Project Management
- Create projects linked to specific clients
- Set project-specific hourly rates
- Track project status (active, completed, paused)
- View project earnings and hours worked

### ⏰ Time Tracking
- Log work sessions with detailed descriptions
- Categorize work by task type (coding, meetings, design)
- View recent work history
- Automatic earnings calculation

### 📊 Business Reports
- Earnings breakdown by client
- Work summary for any time period
- Overall business statistics
- Average hourly rate calculations

## 🛠️ Technologies Used

- **Python 3.8+** - Main programming language
- **SQLAlchemy** - Object-Relational Mapping (ORM)
- **Click** - Command-line interface framework
- **SQLite** - Database for storing data
- **Tabulate** - Beautiful table formatting

## 📋 Requirements Met

✅ **CLI Interface** - Professional command-line interface with organized command groups  
✅ **ORM Functions** - SQLAlchemy models with CRUD operations  
✅ **Object Model** - 4 related classes (Client, Project, TimeEntry, Category)  
✅ **One-to-Many Relationships** - Client→Projects, Project→TimeEntries  
✅ **CLI Best Practices** - Clear commands, help text, error handling  
✅ **OOP Best Practices** - Proper class design, methods, relationships  

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/freelancer-project-tracker.git
cd freelancer-project-tracker
```

### 2. Create Virtual Environment
```bash
python -m venv freelancer_env
source freelancer_env/bin/activate  # Mac/Linux
# OR
freelancer_env\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python main.py --help
```

## 💡 Usage Examples

### Getting Started
```bash
# See all available commands
python main.py --help

# Add your first client
python main.py client add

# Create a project for the client
python main.py project add

# Log time you worked
python main.py time log

# See your earnings
python main.py report earnings
```

### Sample Workflow
```bash
# 1. Add a client
python main.py client add
# Enter: Name: John Doe, Email: john@company.com, Rate: 50

# 2. Create a project
python main.py project add
# Select client and enter project details

# 3. Log work time
python main.py time log
# Select project, enter hours and description

# 4. View your work
python main.py time recent

# 5. Generate earnings report
python main.py report earnings --days 30
```

## 📁 Project Structure
```
freelancer-project-tracker/
│
├── models.py          # Database models (Client, Project, TimeEntry, Category)
├── cli.py            # CLI commands and interface
├── main.py           # Application entry point
├── requirements.txt  # Python dependencies
├── README.md         # This file
├── .gitignore       # Git ignore rules
└── freelancer_tracker.db  # SQLite database (created automatically)
```

## 🗄️ Database Schema

### Entities & Relationships
- **Client** (1) → **Project** (Many): One client can have multiple projects
- **Project** (1) → **TimeEntry** (Many): One project can have multiple time entries
- **Project** (Many) ↔ **Category** (Many): Projects can have multiple categories

### Tables
1. **clients**: id, name, email, company, phone, hourly_rate, created_at
2. **projects**: id, name, description, client_id, hourly_rate, status, deadline, created_at
3. **time_entries**: id, project_id, date_worked, hours, description, task_type, created_at
4. **categories**: id, name, description, created_at

## 🎮 Available Commands

### Client Commands
- `python main.py client add` - Add a new client
- `python main.py client list` - Show all clients

### Project Commands
- `python main.py project add` - Create a new project
- `python main.py project list` - Show all projects
- `python main.py project list --status active` - Show only active projects

### Time Tracking Commands
- `python main.py time log` - Log time worked on a project
- `python main.py time recent` - Show recent work (last 7 days)
- `python main.py time recent --days 30` - Show last 30 days
- `python main.py time recent --project-id 1` - Show time for specific project

### Report Commands
- `python main.py report earnings` - Earnings report (last 30 days)
- `python main.py report earnings --days 7` - Weekly earnings report
- `python main.py report summary` - Overall business summary

## 🎓 Learning Outcomes

Through building this project, I learned:
- **ORM Design**: Creating related database models with SQLAlchemy
- **CLI Development**: Building user-friendly command-line interfaces with Click
- **Database Relationships**: Implementing one-to-many relationships
- **Python OOP**: Proper class design and method implementation
- **Error Handling**: Managing database transactions and user input
- **Code Organization**: Structuring a multi-file Python application

## 🤝 Personal Touch

This project reflects my journey as a student learning both programming and freelancing. I added personal touches like:
- Encouraging messages ("Add your first client!", "You earned $X!")
- Simple, student-friendly language in help text
- Practical features I actually need as a freelancer
- Clear visual feedback with emojis and formatting

## 🐛 Known Limitations

- No user authentication (single-user application)
- SQLite database (suitable for personal use)
- No GUI (command-line only)
- Basic reporting (no charts or graphs)

## 🔮 Future Enhancements

If I had more time, I would add:
- CSV export for accounting software
- Timer start/stop functionality
- Project deadline reminders
- More advanced reporting
- Multi-currency support

## 📝 Author Notes

Created as part of Phase 3 Python CLI project at Moringa School. This represents my learning journey in Python, databases, and software design. The project meets all requirements while being practical for real-world use.

**Contact:** maureen.karimi@student.moringaschool.com

---

*"Every expert was once a beginner. Keep coding!" - Maureen W Karimi* 🚀
