from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import save_data, load_data
from tabulate import tabulate



def add_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")

    try:
        user = User.create(name, email)
        print(f"User created: {user}")
    except (ValueError,TypeError) as error:
        print(f"Error: {error}")

def list_users():
    users = User.all()
    if not users:
        print("\nNo users found.")
        return
    
    user_data = []

    for user in users:
        user_data.append([
            user.user_id,
            user.name,
            user.email
        ])

    print(tabulate(
        user_data,
        headers=["User ID", "Name", "Email"],
        tablefmt="grid"
    ))


def add_project():
    title = input("Please enter the project title: ")
    description = input("Please enter the project description: ")
    due_date = input("Please enter the due date in this format (YYYY-MM-DD): ")

    try:
        project =Project.create(title, description, due_date)
        print("\nProject created successfully!")
        print(project)
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

def list_projects():
    projects = Project.all()

    if not projects:
        print("\n No projects found")
        return
    
    project_data = []

    for project in projects:
        project_data.append([
            project.project_id,
            project.title,
            project.description,
            project.due_date,
            project.user_id if project.user_id else "Not assigned"
        ])

    print(tabulate(
        project_data,
        headers=["Project ID", "Title", "Description", "Due Date", "Assigned User"],
        tablefmt="grid"
    ))

def assign_project():
    user_id = input("Enter user ID: ")
    project_id = input("Enter project ID: ")

    user = User.get(user_id)
    project = Project.get(project_id)

    if user is None:
        print("User not found. ")
        return

    if project is None:
        print("Project not found. ")
        return

    try:
        user.add_project(project)
        print("Project assigned succesfully!")
        print(f"Project with the ID {project.project_id} assigned to {user.name}.")

    except (ValueError, TypeError) as error:
        print("Error: ", error)

def add_task():
    title = input("Enter task title: ")
    user_id = input("Enter the ID of the user: ")
    project_id = input("Enter project ID: ")

    user = User.get(user_id)
    project = Project.get(project_id)

    if user is None:
        print("User not found. ")
        return

    if project is None:
        print("Project not found")
        return

    if project.user_id != user.user_id:
        print("This project is not assigned to that user. ")
        return

    try:
        task = Task.create(title, user.user_id)
        project.add_task(task)

        print("Task created successfuly!")
        print(task)

    except (ValueError, TypeError) as error:
        print("Error:", error)

def list_tasks():
    tasks = Task.all()

    print("\n **** TASKS **** ")

    if not tasks:
        print("No tasks found.")
        return

    task_data = []

    for task in tasks:
        task_data.append([
            task.task_id,
            task.title,
            task.status,
            task.assigned_to,
            task.project_id if task.project_id else "Not assigned"
        ])

    print(tabulate(
        task_data,
        headers=["Task ID", "Title", "Status", "Assigned User", "Project ID"],
        tablefmt="grid"
    ))


def complete_task():
    task_id = input("Enter task ID: ")

    task = Task.get(task_id)

    if task is None:
        print("Task not found")
        return

    if task.status == "completed":
        print("This task is already completed.")
        return

    task.mark_complete()

    print("Task completed successfully!")
    print(task)

def search_projects():
    user_id = input("Enter user ID: ")
    user = User.get(user_id)

    if user is None:
        print("User not found.")
        return

    for project_id in user.project_ids:
        print(Project.get(project_id))

    if not user.project_ids:
        print("No projects assigned to this user.")
  

def main():
    load_data()
    while True:
        print("\n===== PROJECT MANAGEMENT SYSTEM =====")
        print("1. Add User")
        print("2. List Users")
        print("3. Add Project")
        print("4. List Projects")
        print("5. Assign Project to User")
        print("6. Add Task")
        print("7. List Tasks")
        print("8. Complete Task")
        print("9. Search Projects by User")
        print("0. Exit")
        print("=====================================")


        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 9")
            continue

        if choice not in [1,2,3,4,5,6,7,8,9,0]:
            print("Invalid choice")

        elif choice == 1:
            add_user()

        elif choice == 2:
            list_users()

        elif choice == 3:
            add_project()

        elif choice == 4:
            list_projects()

        elif choice == 5:
            assign_project()
                
        elif choice == 6:
            add_task()

        elif choice == 7:
            list_tasks()

        elif choice == 8:
            complete_task()

        elif choice == 9:
            search_projects()

        else:
            save_data()
            print("Goodbye!")
            break
        
        
if __name__ == "__main__":
    main()
