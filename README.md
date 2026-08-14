# Assignment Tracker

## Project Overview

The **Assignment Tracker** is a Python console-based application for managing homework and exam assignments. It allows users to add assignments, view assignments, filter them by month, track completion status, view assignment statistics, and calculate average grades.

The project uses **Object-Oriented Programming (OOP)** with classes for `Assignment`, `Homework`, and `Exam`.

## Features

* Add homework assignments.
* Add exam assignments.
* List all saved assignments.
* Filter assignments by due month.
* Mark assignments as completed.
* View an assignment summary showing:

  * Total assignments
  * Completed and pending homework
  * Completed and pending exams
  * Assignments due within the next 7 and 30 days
* Calculate separate average scores for homework and exams.
* Validate user input for:

  * Assignment scores
  * Maximum scores
  * Due dates
  * Month selection
  * Assignment selection
* Display assignments in a readable format.

## Instructions to Run the Program

### Requirements

* Python 3
* PyCharm or another Python IDE
* All project files should be in the same folder:

  * `main.py`
  * `assignment.py`
  * `homework.py`
  * `exam.py`
  * `subjects.py`

### Running the Program

1. Open the project in PyCharm.
2. Make sure all five Python files are in the same project folder.
3. Open `main.py`.
4. Run `main.py`.
5. The menu will appear in the console.
6. Enter the number corresponding to the desired menu option.

No external Python packages are required.

## Menu Structure

### 1. Add Homework

Creates a new homework assignment. The user is asked to enter:

* Subject name
* Assignment title
* Assignment score
* Maximum score
* Due date

### 2. Add Exam

Creates a new exam assignment using the same information as a homework assignment.

### 3. List Assignments

Displays all homework and exam assignments currently stored in the program.

### 4. Filter by Month

Allows the user to enter a month number from `1` to `12`. The program displays all homework and exams with a due date in the selected month.

Invalid month values and non-numeric inputs are rejected.

### 5. Summary

Displays an overview of the assignments, including:

* Total number of assignments
* Total, completed, and pending homework
* Total, completed, and pending exams
* Number of incomplete assignments due within the next 7 days
* Number of incomplete assignments due within the next 30 days

### 6. Mark Assignment as Completed

Displays all assignments with their current status. The user selects an assignment by entering its number.

The selected assignment is then marked as completed.

This can be confirmed by selecting the summary once an assignment has been marked complete

### 7. Grade Summary

Calculates the average score for homework and exams separately.

The scores are converted to a value out of `1.0`.

If there are no homework or exam assignments, the program displays an appropriate message instead of causing a division-by-zero error.

### 0. Exit

Exits the program and displays:

```text
Goodbye!
```

## Sample Interactions

### Adding a Homework Assignment

```text
Enter your choice(answer should be in form of integer): 1

Enter subject name: Programming
Enter assignment title: Python Assignment
Enter assignment score: 85
Enter maximum score: 100
Enter due date (YYYY-MM-DD): 2026-08-20
```

### Filtering by Month

```text
Enter your choice(answer should be in form of integer): 4

Enter the month number (1-12): 8

Homework:
Python Assignment

Exams:
Database Exam
```

### Marking an Assignment as Completed

```text
Enter your choice(answer should be in form of integer): 6

1. Python Assignment - Pending
2. Database Exam - Pending

Choose an assignment: 1
```

The selected assignment is then marked as completed.

### Viewing the Summary

```text
ASSIGNMENT SUMMARY
Total assignments: 2

Homework
    Total: 1
    Completed: 1
    Pending: 0

Exams
    Total: 1
    Completed: 0
    Pending: 1

Upcoming
    Next 7 days: 1
    Next 30 days: 1
```

### Viewing the Grade Summary

```text
Enter your choice(answer should be in form of integer): 7

Average homework score: 0.85/1.0
Average exam score: 0.72/1.0
```

### Exiting

```text
Enter your choice(answer should be in form of integer): 0

Goodbye!
```
