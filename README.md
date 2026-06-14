# Library Management System

A console-based Library Management System developed using **Python** and **Oracle Database**. The application helps manage library operations such as issuing books, returning books, maintaining transaction records, and updating inventory in real time.

## Features

* Issue books to students
* Return issued books
* Automatic inventory management
* Transaction history tracking
* Database integration with Oracle Database
* Exception handling for invalid operations
* Menu-driven user interface

## Technologies Used

* Python 3.x
* Oracle Database XE
* OracleDB Python Driver (`oracledb`)

## Database Tables

### Books Table

| Column   | Description      |
| -------- | ---------------- |
| book_id  | Unique Book ID   |
| title    | Book Title       |
| author   | Author Name      |
| quantity | Available Copies |

### Library Transactions Table

| Column         | Description           |
| -------------- | --------------------- |
| transaction_id | Unique Transaction ID |
| student_id     | Student ID            |
| book_id        | Issued Book ID        |
| issue_date     | Book Issue Date       |
| return_date    | Book Return Date      |
| status         | ISSUED / RETURNED     |

## Project Workflow

### Issue Book

1. Enter Student ID.
2. Enter Book ID.
3. Check book availability.
4. Create transaction record.
5. Reduce inventory quantity.
6. Commit changes to database.

### Return Book

1. Enter Transaction ID.
2. Verify transaction status.
3. Update return date and status.
4. Increase inventory quantity.
5. Commit changes to database.

## Installation

### Clone Repository

```bash
git clone https://github.com/KOLLENIRANJAN/library-management-system.git
cd library-management-system
```

### Install Dependencies

```bash
pip install oracledb
```

### Configure Database Connection

Update the following values in the source code:

```python
conn = oracledb.connect(
    user="system",
    password="your_password",
    dsn="localhost/XE"
)
```

### Run Application

```bash
python library_management.py
```

## Sample Menu

```text
===== Library Management System =====
1. Issue Book (Log Transaction)
2. Return Book (Replenish Stock)
3. View History Records
4. Exit
```

## Future Enhancements

* Student Management Module
* Book Search Functionality
* Due Date Tracking
* Fine Calculation System
* Admin Authentication
* Graphical User Interface (GUI)
* Report Generation

## Learning Outcomes

* Database Connectivity using Python
* Oracle SQL Operations
* Transaction Management
* CRUD Operations
* Inventory Management Logic
* Exception Handling

## Author

Kolle Niranjan

GitHub: https://github.com/KOLLENIRANJAN
