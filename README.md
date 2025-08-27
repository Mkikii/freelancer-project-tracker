#  Freelancer Project & Time Tracker

**Created by: Maureen W Karimi**  
**Phase 3 Python CLI Project - Moringa School**

A simple command-line application that helps me manage my freelance business by tracking clients, projects, and time worked. Built with Python, SQLAlchemy, and Click.

##  Project Overview

This CLI application solves real freelancer problems:
-  **Client Management**: Store client information and contact details
-  **Project Tracking**: Organize work by projects with different hourly rates
-  **Time Logging**: Track hours worked with detailed descriptions
-  **Earnings Reports**: See how much money you've made
- **Business Analytics**: Get insights into your freelance business

## 🛠Technologies Used

- **Python 3.8+** - Programming language
- **SQLAlchemy** - ORM for database operations
- **Click** - CLI framework for beautiful command-line interfaces
- **Tabulate** - Pretty table formatting
- **SQLite** - Database (no setup required!)

##  Requirements Met

✅ **CLI Interface** - Professional Click-based interface with help text  
✅ **ORM Functions** - Full CRUD operations using SQLAlchemy  
✅ **Object Model** - 4 classes with 4+ attributes each  
✅ **One-to-Many Relationships** - Client→Projects, Project→TimeEntries  
✅ **CLI Best Practices** - Clear commands, error handling, user-friendly output  
✅ **OOP Best Practices** - Methods, relationships, proper encapsulation  

## 🏗 Database Schema

### Models Overview:
1. **Client** - Stores client information (name, email, company, phone)
2. **Project** - Tracks projects (name, hourly rate, description, status)
3. **TimeEntry** - Logs work sessions (hours, description, date)
4. **Category** - Organizes work types (name, description, color)

### Relationships:
- One Client can have Many Projects
- One Project can have Many TimeEntries

##  Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd freelancer-tracker
   ```

2. **Install dependencies**:
   ```bash
   pip install sqlalchemy click tabulate
   ```

3. **Initialize the database**:
   ```bash
   python models.py
   ```

4. **Start using the app**:
   ```bash
   python cli.py --help
   ```

##  How to Use

### 1. Add Your First Client
```bash
python cli.py client add
# Follow the prompts to enter client information
```

### 2. Create a Project
```bash
python cli.py project add
# Link it to a client and set your hourly rate
```

### 3. Log Work Time
```bash
python cli.py time log
# Track hours worked with descriptions
```

### 4. View Reports
```bash
python cli.py summary           # Business overview
python cli.py client list       # All clients
python cli.py project list      # All projects  
python cli.py time recent       # Recent time entries
```

## 📸 Example Usage

```bash
# Add a client
$ python cli.py client add
Client name: Google Inc
Email address: contact@google.com
Company (optional): Google
Phone (optional): +1-650-253-0000
Client 'Google Inc' added successfully!

# Create a project
$ python cli.py project add
Project name: Website Redesign
Client ID: 1
Hourly rate ($) [25.0]: 75.0
Description (optional): Redesign company website with modern UI
 Project 'Website Redesign' created for Google Inc!
💰 Hourly rate: $75.00

# Log time worked
$ python cli.py time log
Project ID: 1
Hours worked: 3.5
What did you work on?: Implemented responsive navigation and hero section
Task type (optional): coding
✅ Time logged successfully!
📊 3.5 hours on 'Website Redesign'
💰 You earned $262.50!

# View summary
$ python cli.py summary
📈 FREELANCE BUSINESS SUMMARY
👥 Total Clients: 3
📁 Total Projects: 5
⏰ Total Hours Worked: 42.5
💰 Total Earnings: $1,837.50
```

##  Features That Make This Special

- **Beginner-Friendly**: Clean code with helpful comments
- **Emoji Usage**: Makes the CLI fun and visually appealing  
- **Error Handling**: Graceful error messages and tips
- **Real-World Practical**: Actually useful for freelancers
- **Beautiful Tables**: Professional output formatting
- **Encouraging Messages**: Positive feedback on actions

##  Advanced Features

- **Flexible Hourly Rates**: Different rates per project
- **Detailed Time Tracking**: Log what you worked on
- **Business Analytics**: See your earning trends
- **Client Relationship**: Track total earnings per client
- **Status Management**: Mark projects as active/completed

##  Learning Objectives Achieved

1. **Database Design** - Proper relationships and constraints
2. **ORM Usage** - SQLAlchemy for all database operations
3. **CLI Development** - Click framework with proper structure
4. **Object-Oriented Programming** - Classes, methods, inheritance
5. **Error Handling** - Try/except blocks and user feedback
6. **Code Organization** - Separate models and CLI logic


##  Future Enhancements

- Export data to CSV/Excel
- Time tracking with start/stop timer
- Invoice generation
- Data visualization with charts
- Multi-currency support
- Backup and restore features

##  About the Developer

**Maureen W Karimi**  
Moringa School - Phase 3 Student  
Passionate about building practical solutions with Python!

## 📄 License

This project is created for educational purposes as part of Moringa School's Python curriculum.

---

*"Building practical solutions, one commit at a time!"* 🚀
