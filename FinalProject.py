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

class TaskStatus:
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

tasks = []

def add_task():
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    status = TaskStatus.TODO

    new_task = Task(title, description, status)
    tasks.append(new_task)
    print("Task added.")

def get_task_by_id(id):
    for task in tasks:
        if task.task_id == id:
            return task
    return None


def read_user_input():
    while True:
        print("\nChoose an option:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Remove task")
        print("5. Exit")

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
            # Caleb implement edit_task() function
            print("Edit task not implemented yet.")

        elif choice == "4":
            # Peter implement remove_task() function
            print("Remove task not implemented yet.")

        elif choice == "5":
            # Peter implement Exit
            print("Exiting...")
            break

# Peter - implement file reading: converting JSON to Task[]
# Caleb - implement file writing: converting Task[] to JSON