

# Student Management System

A simple, menu-driven Student Management System built using Python to manage student records, calculate percentages, and perform basic record management operations.

## About

This project is a console-based application that allows users to manage up to **10 student records**. Users can add student details, view all registered students, search for a student, update student information, and delete student records.

The system calculates each student's percentage based on their obtained marks and total marks.

## Features

- Add student records
- Display all registered students
- Search students by roll number
- Update student details
- Delete student records
- Store student names and roll numbers
- Record obtained marks and total marks
- Calculate student percentages
- Prevent duplicate roll numbers
- Validate marks and total marks
- Limit the system to 10 students
- Handle invalid menu choices

## Technologies Used

- Python

## Python Concepts Practiced

- Variables and data types
- Lists
- Dictionaries
- Functions
- `while` loops
- `for` loops
- Conditional statements
- User input using `input()`
- Type conversion using `float()`
- List methods such as `append()` and `remove()`
- Dictionary operations
- F-strings
- The `round()` function
- Arithmetic operations
- Input validation

## How It Works

### 1. Add Student

The user enters a student's roll number, name, obtained marks, and total marks. The system checks for duplicate roll numbers and validates the marks before saving the record.

### 2. Show All Students

Displays all registered students, including their roll numbers, names, obtained marks, and percentages.

### 3. Search Student

Allows the user to find a student using their roll number and view their complete marks information.

### 4. Update Student

Allows the user to update a student's name, obtained marks, and total marks. The percentage is recalculated automatically.

### 5. Delete Student

Removes a student record from the system using the student's roll number.

## Percentage Calculation

The system calculates the percentage using this formula:

```text
Percentage = (Obtained Marks / Total Marks) × 100
```

**Example:**

- Obtained marks: 450
- Total marks: 500
- Percentage: 90%

The percentage is rounded to two decimal places.

## Menu Options

| Option | Function |
|---|---|
| 0 | Exit |
| 1 | Add Student |
| 2 | Show All Students |
| 3 | Search Student |
| 4 | Update Student |
| 5 | Delete Student |

## Purpose

This project was created to practice Python programming fundamentals by building a practical student record management application.
