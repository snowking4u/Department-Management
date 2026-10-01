# Department Management System (DMS)

## Government Polytechnic Hamirpur --- Department of Computer Engineering

A simple, user-friendly web-based **Department Management System (DMS)**
designed for the Computer Engineering Department of Government
Polytechnic Hamirpur.

The system provides separate role-based access for:

-   **HOD**
-   **Faculty**
-   **Student**

The main purpose of the project is to bring common departmental
activities such as student management, faculty work, attendance,
assignments, notices, timetable, academic information, and departmental
communication into one simple system.

------------------------------------------------------------------------

## 1. Project Overview

In a college department, information is often managed through separate
registers, spreadsheets, notices, messages, and manual communication.

The Department Management System provides a single platform where
different users can access the information and functions relevant to
their role.

### Main idea

``` text
                    Department Management System
                              |
             +----------------+----------------+
             |                |                |
            HOD            Faculty          Student
             |                |                |
       Department         Teaching &        Academic
       Management         Evaluation        Information
```

The system follows a **role-based access** approach. A user can access
only the sections intended for their role.

------------------------------------------------------------------------

# 2. Objectives

The main objectives of the project are:

1.  Provide a centralized departmental management system.
2.  Provide separate login access for HOD, Faculty, and Students.
3.  Reduce manual departmental work.
4.  Make academic information easier to access.
5.  Provide attendance management.
6.  Provide assignment and marks management.
7.  Provide notices and announcements.
8.  Provide timetable and schedule information.
9.  Allow the HOD to monitor department-level information.
10. Keep the system simple enough to maintain and understand.

------------------------------------------------------------------------

# 3. User Roles

## HOD

The HOD has department-level management and monitoring access.

### HOD Features

-   Dashboard
-   Student Management
-   Faculty Management
-   Subject/Course Management
-   Timetable Management
-   Attendance Overview
-   Notices & Announcements
-   Events Management
-   Leave/Request Approval
-   Reports & Analytics
-   Department Documents
-   Profile
-   Settings
-   Logout

### HOD Dashboard

The dashboard can display:

-   Total Students
-   Total Faculty
-   Average Attendance
-   Active Subjects
-   Today's Schedule
-   Pending Requests
-   Recent Notices
-   Upcoming Events
-   Attendance Overview
-   Quick Actions

### HOD Responsibilities

The HOD can monitor departmental activities and manage department-level
information.

------------------------------------------------------------------------

# 4. Faculty Module

Faculty members use the system for teaching, attendance, assignments,
academic evaluation, and communication.

## Faculty Features

-   Faculty Dashboard
-   My Classes
-   My Students
-   My Subjects
-   Attendance
-   Assignments
-   Marks / Results
-   Study Material
-   Timetable
-   Notices
-   Student Information
-   Profile
-   Logout

### Faculty Dashboard

The dashboard can contain:

-   Today's Classes
-   Total Assigned Students
-   Attendance Average
-   Pending Assignments
-   Today's Schedule
-   Pending Tasks
-   Recent Notices
-   Quick Actions

### Attendance

Faculty can:

-   Select a class
-   Select a subject
-   Mark attendance
-   View attendance
-   View attendance history

### Assignments

Faculty can:

-   Create assignments
-   Set assignment title
-   Add description
-   Set submission date
-   View assignment status
-   View student submissions

### Marks

Faculty can:

-   Enter internal marks
-   Update marks
-   View student performance

### Study Material

Faculty can:

-   Upload notes
-   Upload study material
-   Manage existing material

------------------------------------------------------------------------

# 5. Student Module

Students use the system to access their academic information and
communicate with the department.

## Student Features

-   Student Dashboard
-   My Profile
-   My Subjects
-   My Attendance
-   My Assignments
-   Assignment Submission
-   Marks / Results
-   Study Material
-   Timetable
-   Notices & Announcements
-   Events
-   Leave Request
-   Documents
-   Notifications
-   Logout

### Student Dashboard

The dashboard can display:

-   Today's Classes
-   Attendance Percentage
-   Pending Assignments
-   Recent Notices
-   Upcoming Events
-   Latest Academic Information

### Student Attendance

Students can view:

-   Subject-wise attendance
-   Overall attendance
-   Attendance history

Students cannot directly modify their attendance.

------------------------------------------------------------------------

# 6. Login & Authentication

The project uses a common login system with three roles:

``` text
                 LOGIN
                   |
          +--------+--------+
          |        |        |
         HOD    Faculty   Student
          |        |        |
       Dashboard Dashboard Dashboard
```

The login page contains:

-   Role selection
-   Email / ID
-   Password
-   Show/Hide Password
-   Remember Me
-   Forgot Password
-   Login button

The backend verifies the user's credentials and role before creating a
login session.

### Security

Passwords should never be stored as plain text.

The project uses password hashing with Werkzeug.

The backend is responsible for checking the actual role of the logged-in
user.

------------------------------------------------------------------------

# 7. Technology Stack

## Backend

-   Python
-   Flask
-   Flask-SQLAlchemy

## Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Jinja2 Templates

## Database

-   SQLite
-   SQLAlchemy ORM

## Development

-   Git
-   GitHub
-   VS Code / similar code editor


------------------------------------------------------------------------

# 8. Project Structure

``` text
Department-Management-System/
│
├── instance/
│   └── database.db
│
├── static/
│   ├── images/
│   ├── js/
│   ├── Style.css
│   ├── admin.css
│   └── login.css
│
├── templates/
│   ├── login.html
│   │
│   ├── hod/
│   │   ├── dashboard.html
│   │   ├── students.html
│   │   ├── faculty.html
│   │   ├── subjects.html
│   │   ├── timetable.html
│   │   ├── attendance.html
│   │   ├── notices.html
│   │   ├── events.html
│   │   ├── requests.html
│   │   └── reports.html
│   │
│   ├── faculty/
│   │   ├── dashboard.html
│   │   ├── classes.html
│   │   ├── attendance.html
│   │   ├── assignments.html
│   │   ├── marks.html
│   │   ├── materials.html
│   │   └── profile.html
│   │
│   └── student/
│       ├── dashboard.html
│       ├── attendance.html
│       ├── assignments.html
│       ├── marks.html
│       ├── materials.html
│       ├── timetable.html
│       └── profile.html
│
├── main.py
├── requirements.txt
├── README.md
└── Dockerfile
```

The actual folder structure may be simplified during development.

------------------------------------------------------------------------

# 9. Basic Application Flow

## Login

``` text
User
 |
 v
Login Page
 |
 v
Enter ID/Email + Password
 |
 v
Flask Login Route
 |
 v
Check Database
 |
 v
Verify Password
 |
 v
Check Role
 |
 +--------+---------+
 |        |         |
HOD    Faculty   Student
 |        |         |
 v        v         v
HOD     Faculty   Student
Dashboard Dashboard Dashboard
```

------------------------------------------------------------------------

# 10. HOD Workflow

``` text
HOD Login
   |
   v
HOD Dashboard
   |
   +--> Manage Students
   |
   +--> Manage Faculty
   |
   +--> Manage Subjects
   |
   +--> Timetable
   |
   +--> Attendance Overview
   |
   +--> Notices
   |
   +--> Events
   |
   +--> Requests
   |
   +--> Reports
```

------------------------------------------------------------------------

# 11. Faculty Workflow

``` text
Faculty Login
      |
      v
Faculty Dashboard
      |
      +--> My Classes
      |
      +--> Attendance
      |
      +--> Assignments
      |
      +--> Marks
      |
      +--> Study Material
      |
      +--> Timetable
      |
      +--> Notices
```

------------------------------------------------------------------------

# 12. Student Workflow

``` text
Student Login
      |
      v
Student Dashboard
      |
      +--> Attendance
      |
      +--> Assignments
      |
      +--> Marks
      |
      +--> Study Material
      |
      +--> Timetable
      |
      +--> Notices
      |
      +--> Leave Request
```
------------------------------------------------------------------------

# 13. Installation

Clone the repository:

``` bash
git clone https://github.com/snowking4u/Department-Management
```

Enter the project:

``` bash
cd Department-Management
```

Create a virtual environment if required:

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run the application:

``` bash
python app.py
```

The Flask development server will start on the configured port.

The SQLite database will be created automatically when the application
creates its tables.

------------------------------------------------------------------------
# 14. Future Scope

The project can be expanded in the future with:

-   Email notifications
-   SMS notifications
-   Online fee information
-   Exam management
-   Library integration
-   Placement management
-   Hostel management
-   Parent/Guardian access
-   Mobile application
-   Advanced analytics
-   Cloud deployment
-   Backup and restore
-   More detailed permission management

These features are outside the initial project scope and should not be
implemented unless required.

------------------------------------------------------------------------

# 15. Project Vision

The long-term vision of the Department Management System is to provide a
simple digital platform for managing the daily academic and
administrative activities of a college department.

The system is designed around three principles:

``` text
        SIMPLE
          +
     USER FRIENDLY
          +
     EASY TO MAINTAIN
          =
 Department Management System
```

The project focuses on solving real departmental problems without
unnecessary technical complexity.

------------------------------------------------------------------------

## License

This project is developed as an academic/college project for the
Department of Computer Engineering, Government Polytechnic Hamirpur.
