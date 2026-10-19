# Project Management System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Local Setup](#local-setup)
- [Usage Guide](#usage-guide)
- [Known Issues](#known-issues)
- [Potential Improvements](#potential-improvements)
- [License](#license)

## Overview
**Project Management System** is a beginner-friendly Python command-line program for keeping track of users, their projects, and the tasks inside those projects. A numbered menu lets the user add users and projects, assign a project to a user, add tasks, mark tasks as complete, and look up the projects that belong to a user. Everything is saved to a JSON file so the data is still there the next time the program runs.

### Purpose
- Practice object-oriented programming in Python — classes, inheritance, properties with validation, and class methods
- Show how objects that belong to each other (users own projects, projects own tasks) can be linked together by ID
- Show how to save and load program data with JSON
- Practice using a third-party package from PyPI (`tabulate`) to display clean tables in the terminal

## Features

### Core Features
- **Add and List Users** — each user has a name and a validated email address, and gets an ID such as `USR1001`
- **Add and List Projects** — each project has a title, a description, and a due date in `YYYY-MM-DD` format, and gets an ID such as `PROJ1001`
- **Assign a Project to a User** — a project can belong to only one user
- **Add Tasks** — a task can only be added to a project that is assigned to the chosen user, and gets an ID such as `TASK1001`
- **Complete Tasks** — change a task's status from `pending` to `completed`
- **Search Projects by User** — see every project assigned to a particular user
- **Saved Data** — users, projects, and tasks are written to `data/data.json` when the program exits and loaded again at start-up

### User Experience Features
- **Menu-Driven Interface** — a numbered menu that repeats until the user chooses to exit
- **Readable Tables** — users, projects, and tasks are shown in tables (using `tabulate`)
- **Input Validation** — empty titles, bad email addresses, wrongly formatted dates, and non-numeric menu choices show a friendly message instead of crashing
- **Clear Messages** — the program says when a user, project, or task cannot be found, and when a task is already completed

## Technologies Used

### Language
- **Python 3** — the whole program is written in Python

### Standard Library
- **`json`** — saving and loading the data file
- **`re`** — checking that an email address has a valid format
- **`datetime`** — checking that a due date is a real date in `YYYY-MM-DD` format

### Third-Party Packages
- **`tabulate`** — prints data as neat tables in the terminal (installed with `pip`, listed in `requirements.txt`)

## Project Structure

```
project-folder/
├── main.py               # the menu and the functions the menu calls
├── models/
│   ├── person.py         # Person base class
│   ├── user.py           # User class (inherits from Person)
│   ├── project.py        # Project class
│   └── task.py           # Task class
├── utils/
│   └── storage.py        # save_data() and load_data()
├── data/
│   └── data.json         # saved data (created when the program exits)
├── requirements.txt
└── README.md
```

The program is built from four classes:

| Class | Main attributes | Main methods |
|---|---|---|
| `Person` | `name` (must be text) | — |
| `User` (inherits `Person`) | `user_id`, `email` (validated), `project_ids` | `create`, `get`, `all`, `add_project`, `to_dict`, `from_dict` |
| `Project` | `project_id`, `title`, `description`, `due_date` (validated), `user_id`, `task_ids` | `create`, `get`, `all`, `add_task`, `to_dict`, `from_dict` |
| `Task` | `task_id`, `title`, `status` (`pending` or `completed`), `assigned_to`, `project_id` | `create`, `get`, `all`, `mark_complete`, `to_dict`, `from_dict` |

- Each class keeps its own collection of objects and its own ID counter, so IDs never repeat (`USR1001`, `USR1002`, ...)
- `to_dict()` and `from_dict()` turn objects into plain dictionaries and back, which is how they are written to and read from JSON
- `save_data()` and `load_data()` in `utils/storage.py` handle the file
- `main.py` shows the menu in a `while` loop and calls the right function for the chosen option

## Local Setup

### Requirements
- Python 3.8 or higher
- A terminal or command prompt

### Installation
1. Clone the repository:
   ```
   git clone <your-repo-url>
   ```
2. Navigate into the project directory:
   ```
   cd <your-project-folder>
   ```
3. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   On Windows, activate it with `.venv\Scripts\activate` instead.
4. Install the required package:
   ```
   pip install -r requirements.txt
   ```
5. Make sure the `data/` folder exists in the project folder (it is where the saved data goes)
6. Run the program from inside the project folder:
   ```
   python3 main.py
   ```

Run the program from the project folder every time. The data file is found using a path relative to where you start the program.

## Usage Guide

When the program starts, it shows this menu:

```
===== PROJECT MANAGEMENT SYSTEM =====
1. Add User
2. List Users
3. Add Project
4. List Projects
5. Assign Project to User
6. Add Task
7. List Tasks
8. Complete Task
9. Search Projects by User
0. Exit
=====================================
Choose an option:
```

Type a number from 0 to 9 and press Enter. After each action the menu appears again.

### Adding a User
1. Choose option **1**
2. Enter the user's name and email address
3. The program shows the new user and their ID, for example `USR1001`

### Listing Users
1. Choose option **2** to see all users in a table

### Adding a Project
1. Choose option **3**
2. Enter the title, the description, and the due date as `YYYY-MM-DD`
3. The program shows the new project and its ID, for example `PROJ1001`

### Listing Projects
1. Choose option **4** to see all projects in a table, including who each one is assigned to (or "Not assigned")

### Assigning a Project to a User
1. Choose option **5**
2. Enter the user ID and the project ID exactly as shown in the tables
3. A project that already belongs to another user cannot be assigned to a second user

### Adding a Task
1. Choose option **6**
2. Enter the task title, the user ID, and the project ID
3. The project must already be assigned to that user, otherwise the program says so and does not create the task

### Listing Tasks
1. Choose option **7** to see all tasks in a table with their status, assigned user, and project

### Completing a Task
1. Choose option **8**
2. Enter the task ID
3. The status changes to `completed`. Completing a task that is already completed shows a message instead

### Searching Projects by User
1. Choose option **9**
2. Enter a user ID to see the projects assigned to that user

### Exiting
1. Choose option **0** to save the data to `data/data.json`, print "Goodbye!", and close the program

### Example Session
```
Choose an option: 1
Enter user name: Jane Doe
Enter user email: jane@example.com
User created: User(user_id='USR1001', name='Jane Doe', email='jane@example.com')

Choose an option: 3
Please enter the project title: Website Redesign
Please enter the project description: Update the company website
Please enter the due date in this format (YYYY-MM-DD): 2026-12-01

Project created successfully!
Project(project_id='PROJ1001', title='Website Redesign')

Choose an option: 5
Enter user ID: USR1001
Enter project ID: PROJ1001
Project assigned succesfully!
Project with the ID PROJ1001 assigned to Jane Doe.

Choose an option: 6
Enter task title: Design homepage
Enter the ID the user: USR1001
Enter project ID: PROJ1001
Task created successfuly!
Task(task_id='TASK1001', title='Design homepage', status='pending')

Choose an option: 8
Enter task ID: TASK1001
Task completed successfully!
Task(task_id='TASK1001', title='Design homepage', status='completed')

Choose an option: 7

 **** TASKS **** 
+-----------+-----------------+-----------+-----------------+--------------+
| Task ID   | Title           | Status    | Assigned User   | Project ID   |
+===========+=================+===========+=================+==============+
| TASK1001  | Design homepage | completed | USR1001         | PROJ1001     |
+-----------+-----------------+-----------+-----------------+--------------+

Choose an option: 0
Data saved successfully
Goodbye!
```
Run the program again and the same user, project, and task are loaded from `data/data.json`.

## Known Issues
- **Data is only saved when you choose Exit (option 0).** If the program is closed any other way, such as closing the terminal window or pressing Ctrl+C, the changes from that session are lost
- **A damaged or empty `data/data.json` stops the program at start-up.** Delete the file to start fresh
- **IDs must be typed exactly.** `USR1001` works but `usr1001` is not found
- **ID numbers can skip.** An attempt to create a user, project, or task that fails validation (for example, a bad email) still uses up an ID number
- **Duplicate emails are allowed.** Two users can have the same email address
- **Past due dates are accepted.** Only the date format is checked

## Potential Improvements
- **Save After Every Change** — write to the data file after each action instead of only on exit
- **Command-Line Commands** — use `argparse` so actions can be run directly, such as `add-user` or `complete-task`
- **Case-Insensitive IDs** — accept `usr1001` as well as `USR1001`
- **Duplicate Email Check** — refuse to create a user with an email that already exists
- **Edit and Delete** — change or remove users, projects, and tasks
- **Filters** — show only the tasks of one project, or only pending tasks
- **Friendlier Output** — show projects returned by "Search Projects by User" in a table, like the other lists
- **Automated Tests** — add unit tests for each class, including the validation rules

## License

MIT License

Copyright © 2026 Dennis Sambu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
