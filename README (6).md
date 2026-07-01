# 📝 Command-Line To-Do List Application

A beginner-friendly, terminal-based To-Do List manager built with **pure Python** — no external libraries required.

---

## 📌 Project Overview

This project is a simple yet complete task management application that runs in the command line. It allows users to add, view, and delete tasks interactively through a menu-driven interface. Built as part of a **Level 2 Python Development Internship**, this project demonstrates core Python programming concepts in a practical, real-world-style application.

---

## ✨ Features

- ✅ Add one or multiple tasks
- 📋 View all tasks with serial numbers
- 🗑️ Delete any task by its serial number
- 🔄 Continuous loop until the user chooses to exit
- ⚠️ Graceful handling of invalid inputs (wrong menu choice, empty task, out-of-range number)
- 🧹 Clean, well-commented, readable code

---

## 🛠️ Technologies Used

| Technology | Details |
|---|---|
| Language | Python 3.x |
| Libraries | None (core Python only) |
| Interface | Command-Line (Terminal) |
| Data Storage | Python `list` (in-memory) |

---

## 📁 Project Structure

```
todo-app/
│
└── todo_app.py       # Main application file
└── README.md         # Project documentation
```

---

## ▶️ How to Run

### Prerequisites
- Python 3.x installed on your system

### Steps

1. Clone or download the project:
   ```bash
   git clone https://github.com/your-username/todo-app.git
   cd todo-app
   ```

2. Run the application:
   ```bash
   python todo_app.py
   ```
   > On some systems, use `python3 todo_app.py`

---

## 🖥️ Sample Input & Output

```
Welcome to the To-Do List App! 🎯

========================================
       📝  TO-DO LIST APPLICATION
========================================
  1. Add Task
  2. View Tasks
  3. Delete Task
  4. Exit
========================================
Enter your choice (1-4): 1

Enter the task: Buy groceries
✅  Task 'Buy groceries' added successfully!

Enter your choice (1-4): 2

----------------------------------------
         YOUR TASKS
----------------------------------------
  1. Buy groceries
----------------------------------------

Enter your choice (1-4): 3

  1. Buy groceries

Enter the task number to delete: 1
🗑️   Task 'Buy groceries' deleted successfully!

Enter your choice (1-4): 4
👋  Thank you for using the To-Do List App. Goodbye!
```

---

## 📚 Concepts Demonstrated

- Functions and modular code design
- Python `list` operations (`append`, `pop`, `enumerate`)
- `while` loop for continuous menu
- `try-except` for error handling
- `f-strings` for formatted output
- Input validation
- `if __name__ == "__main__"` pattern

---

## 👨‍💻 Author

**Python Development Internship – Level 2**

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
