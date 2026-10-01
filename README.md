Department Management System (DMS)
Government Polytechnic Hamirpur --- Department of Computer Engineering
A simple, user-friendly web-based Department Management System (DMS)
designed for the Computer Engineering Department of Government
Polytechnic Hamirpur.
The system provides separate role-based access for:
HOD
Faculty
Student
The main purpose of the project is to bring common departmental
activities such as student management, faculty work, attendance,
assignments, notices, timetable, academic information, and departmental
communication into one simple system.
---
1. Project Overview
In a college department, information is often managed through separate
registers, spreadsheets, notices, messages, and manual communication.
The Department Management System provides a single platform where
different users can access the information and functions relevant to
their role.
Main idea
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
The system follows a role-based access approach. A user can access
only the sections intended for their role.
---
2. Objectives
The main objectives of the project are:
Provide a centralized departmental management system.
Provide separate login access for HOD, Faculty, and Students.
Reduce manual departmental work.
Make academic information easier to access.
Provide attendance management.
Provide assignment and marks management.
Provide notices and announcements.
Provide timetable and schedule information.
Allow the HOD to monitor department-level information.
Keep the system simple enough to maintain and understand.
---
3. User Roles
3.1 HOD
The HOD has department-level management and monitoring access.
HOD Features
Dashboard
Student Management
Faculty Management
Subject/Course Management
Timetable Management
Attendance Overview
Notices & Announcements
Events Management
Leave/Request Approval
Reports & Analytics
Department Documents
Profile
Settings
Logout
HOD Dashboard
The dashboard can display:
Total Students
Total Faculty
Average Attendance
Active Subjects
Today's Schedule
Pending Requests
Recent Notices
Upcoming Events
Attendance Overview
Quick Actions
HOD Responsibilities
The HOD can monitor departmental activities and manage department-level
information.
---
4. Faculty Module
Faculty members use the system for teaching, attendance, assignments,
academic evaluation, and communication.
Faculty Features
Faculty Dashboard
My Classes
My Students
My Subjects
Attendance
Assignments
Marks / Results
Study Material
Timetable
Notices
Student Information
Profile
Logout
Faculty Dashboard
The dashboard can contain:
Today's Classes
Total Assigned Students
Attendance Average
Pending Assignments
Today's Schedule
Pending Tasks
Recent Notices
Quick Actions
Attendance
Faculty can:
Select a class
Select a subject
Mark attendance
View attendance
View attendance history
Assignments
Faculty can:
Create assignments
Set assignment title
Add description
Set submission date
View assignment status
View student submissions
Marks
Faculty can:
Enter internal marks
Update marks
View student performance
Study Material
Faculty can:
Upload notes
Upload study material
Manage existing material
---
5. Student Module
Students use the system to access their academic information and
communicate with the department.
Student Features
Student Dashboard
My Profile
My Subjects
My Attendance
My Assignments
Assignment Submission
Marks / Results
Study Material
Timetable
Notices & Announcements
Events
Leave Request
Documents
Notifications
Logout
Student Dashboard
The dashboard can display:
Today's Classes
Attendance Percentage
Pending Assignments
Recent Notices
Upcoming Events
Latest Academic Information
Student Attendance
Students can view:
Subject-wise attendance
Overall attendance
Attendance history
Students cannot directly modify their attendance.
---
6. Login & Authentication
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
Role selection
Email / ID
Password
Show/Hide Password
Remember Me
Forgot Password
Login button
The backend verifies the user's credentials and role before creating a
login session.
Security
Passwords should never be stored as plain text.
The project uses password hashing with Werkzeug.
The backend is responsible for checking the actual role of the logged-in
user.
---
7. Technology Stack
Backend
Python
Flask
Flask-SQLAlchemy
Frontend
HTML5
CSS3
JavaScript
Jinja2 Templates
Database
SQLite
SQLAlchemy ORM
Development
Git
GitHub
VS Code / similar code editor
---
8. Important Architecture Rule
This project intentionally uses a simple Flask architecture.
The project does not use a REST API architecture.
Frontend and backend communicate through:
Flask routes
HTML forms
`request.form`
`request.args`
`render_template()`
`redirect()`
`url_for()`
Flask sessions
Jinja2 templates
Example:
``` text
HTML Form
    |
    v
Flask Route
    |
    v
Validation
    |
    v
SQLAlchemy
    |
    v
SQLite Database
```
This keeps the project understandable for the student development team.
---
9. Database
The database is SQLite.
Database file:
``` text
instance/database.db
```
SQLAlchemy is used to create and access database models.
The database should contain only the tables required by the project.
Possible core models include:
``` text
User
Student
Faculty
Subject
Attendance
Assignment
Marks
Notice
Event
Timetable
LeaveRequest
StudyMaterial
Document
```
The exact database structure can be expanded as development progresses.
---
10. Basic User Model
A common user model can contain:
Field      Purpose
---
id         Unique user ID
name       User name
email      Login email
password   Hashed password
role       HOD / Faculty / Student
Example:
``` python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
```
---
11. Suggested Project Structure
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
---
12. Basic Application Flow
Login
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
---
13. HOD Workflow
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
---
14. Faculty Workflow
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
---
15. Student Workflow
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
---
16. Role Permissions
Feature              HOD                  Faculty                    Student
---
Dashboard            Yes                  Yes                        Yes
Student Management   Full                 Assigned Students          Own Information
Faculty Management   Full                 No                         No
Subject Management   Full                 View Assigned              View
Attendance           View/Manage          Mark/View                  View Own
Assignments          Monitor              Create/Manage              View/Submit
Marks                Monitor              Enter/Manage               View Own
Study Material       Manage/Monitor       Upload/Manage              View
Timetable            Manage               View                       View
Notices              Create/Manage        Class Notices              View
Events               Manage               View                       View
Leave Requests       Approve              View/Process if assigned   Submit
Reports              Department Reports   Class Reports              Own Academic Data
Profile              Own Profile          Own Profile                Own Profile
---

---
17. Installation
Clone the repository:
``` bash
git clone <repository-url>
```
Enter the project:
``` bash
cd Department-Management-System
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
python main.py
```
The Flask development server will start on the configured port.
The SQLite database will be created automatically when the application
creates its tables.
---
18. Basic Requirements
Example `requirements.txt` dependencies:
``` text
Flask
Flask-SQLAlchemy
Werkzeug
```
Additional packages should only be added when they are actually required
by the project.
---

19. Future Scope
The project can be expanded in the future with:
Email notifications
SMS notifications
Online fee information
Exam management
Library integration
Placement management
Hostel management
Parent/Guardian access
Mobile application
Advanced analytics
Cloud deployment
Backup and restore
More detailed permission management
These features are outside the initial project scope and should not be
implemented unless required.
---
20. Project Vision
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

License
This project is developed as an academic/college project for the
Department of Computer Engineering, Government Polytechnic Hamirpur.