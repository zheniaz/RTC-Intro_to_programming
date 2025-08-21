import uuid
from datetime import datetime

class Task:
    def __init__(self, title, description, status):
        self.task_id =  str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.title} ({self.status}) - {self.created_at} - {self.updated_at} - {self.task_id}"

"""
class TaskStatus:
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
"""

taskStatus = [
    "todo", #to do status
    "in_progress", #in progress status
    "done", #done status
]

tasks = []

def add_task():
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    #status = TaskStatus.TODO
    status = taskStatus[0]

    new_task = Task(title, description, status)
    tasks.append(new_task)
    print("Task added.")

def edit_task(which_task):
    print(
        "\nChoose an option:\n"
        "1. Change status\n"
        "2. Change name"
    )
    choice = input("Enter your choice: ").strip()
    while choice not in ["1", "2"]:
        print("Invalid selection.")
        choice = input("Enter your choice: ").strip()

    print("Editing task ", tasks[which_task].title)
    if choice == "1":
        print("Current status: ", tasks[which_task].status)
        print(
            "\nStatus Options:"
            "\n1. todo"
            "\n2. in progress"
            "\n3. done"
        )
        newStatus = input("Enter new status: ").strip()
        while not newStatus.isdigit():
            print("Invalid status.")
            newStatus = input("Enter new status: ").strip()

        tasks[which_task].status = taskStatus[int(newStatus)-1]
    elif choice == "2":
        tasks[which_task].title = input("Enter new task title: ").strip()
        tasks[which_task].description = input("Enter new task description: ").strip()

    print("Task updated.")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    task_id = input("Enter task ID to remove: ").strip()
    task = get_task_by_id(task_id)

    if task:
        tasks.remove(task)
        print(f"Task '{task.title}' removed.")
    else:
        print("No task found with that ID.")

def exit_program():
    print("Exiting...")
    exit()

def get_task_by_id(id):
    for task in tasks:
        if task.task_id == id:
            return task
    return None

# used in bool form only (eg print(assure_string("HELLO")))
def assure_string(prompt):
    string = input(str(prompt))
    while string == "":
        string = input(prompt)
    return string

def read_user_input():
    while True:
        print(
            "\nChoose an option:\n"
            "1. View tasks\n"
            "2. Add task\n"
            "3. Edit task\n"
            "4. Remove task\n"
            "5. Exit"
        )



        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if not tasks:
                print("No tasks available.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

        elif choice == "2":
            add_task()

        elif choice == "3":
            which = input("Enter task name or number: ")

            # If input is a number
            if which.isdigit():
                index = int(which) - 1  # user sees 1-based, we store 0-based
                if 0 <= index < len(tasks):
                    edit_task(index)
                else:
                    print("Invalid task number.")

            # If input is task title
            else:
                index = next((i for i, t in enumerate(tasks) if t.title == which), None)
                if index is not None:
                    edit_task(index)
                else:
                    print("Invalid task name.")

        elif choice == "4":
            # Peter implement remove_task() function
            remove_task()

        elif choice == "5":
            # Peter implement Exit
            remove_task()
            break

read_user_input() # runs the main loop
