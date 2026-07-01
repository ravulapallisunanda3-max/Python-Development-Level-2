import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n===== YOUR TASKS =====")
    for i, t in enumerate(tasks, start=1):
        status = "Completed" if t["completed"] else "Pending"
        print(f"{i}. {t['task']} [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter task number: "))
        if 1 <= n <= len(tasks):
            tasks[n-1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter task number to delete: "))
        if 1 <= n <= len(tasks):
            removed = tasks.pop(n-1)
            save_tasks(tasks)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
