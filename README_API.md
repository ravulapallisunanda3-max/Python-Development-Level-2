# 🌐 API Integration – Command-Line Data Explorer

A professional, menu-driven terminal application that fetches and displays live data from a public REST API using Python 3 and the `requests` library.

---

## 📌 Project Description

This project demonstrates real-world API consumption in Python. It connects to the **JSONPlaceholder** free REST API and retrieves Posts, Users, and Comments. The data is displayed in a clean, formatted terminal interface with full error handling for network failures, timeouts, and HTTP errors.

Built as part of a **Level 2 Python Development Internship**, this project covers intermediate Python concepts including modular programming, exception handling, input validation, and REST API integration.

---

## ✨ Features

| Feature | Details |
|---|---|
| View Posts | Fetch and display all 100 posts |
| View Users | Fetch and display all 10 users with full profiles |
| View Comments | Fetch and display first 10 of 500 comments |
| Search Post by ID | Fetch a specific post (1–100) |
| Search User by ID | Fetch a specific user profile (1–10) |
| Refresh / Test | Ping the API and show response time in ms |
| Error Handling | No internet, timeout, HTTP 404/500, invalid JSON |
| Input Validation | Non-numeric input, out-of-range IDs, empty input |
| Welcome Banner | ASCII art banner on startup |
| Loading Messages | Animated dots while fetching |

---

## 🛠️ Technologies Used

| Technology | Details |
|---|---|
| Language | Python 3.x |
| Library | `requests` (HTTP client) |
| API | JSONPlaceholder – https://jsonplaceholder.typicode.com |
| Interface | Command-Line Terminal |
| Standards | PEP 8, modular programming |

---

## 📁 Folder Structure

```
API_Integration/
│
├── api_integration.py    # Main application (all logic)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📦 Required Python Libraries

```
requests
```

---

## ⚙️ Installation Steps

### 1. Clone the repository
```bash
git clone https://github.com/your-username/api-integration.git
cd api-integration
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install requests
```

---

## ▶️ How to Run

```bash
python api_integration.py
```

Make sure you have an **active internet connection** before running.

---

## 🖥️ Sample Input & Output

```
══════════════════════════════════════════════════════════
       🌐  API INTEGRATION – Data Explorer v1.0
       📡  Source : JSONPlaceholder REST API
══════════════════════════════════════════════════════════

────────────────────────────────────────
          📋  MAIN MENU
────────────────────────────────────────
  1. 📰  View Posts
  2. 👤  View Users
  3. 💬  View Comments
  4. 🔍  Search Post by ID
  5. 🔍  Search User by ID
  6. 🔄  Refresh / Test Connection
  7. ❌  Exit
────────────────────────────────────────
  Enter your choice (1–7): 4

  Enter Post ID to search (1 – 100):
  → 5

  ⏳ Searching for Post #5...
  ✅  Post #5 found!

  ID      : 5
  User ID : 1
  Title   : Nesciunt quas odio
  Body:
    repudiandae veniam quaerat sunt sed alias aut...
```

---

## 👨‍💻 Author

**Python Development Internship – Level 2**

## 📜 License

Open source under the MIT License.
