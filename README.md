# 🚀 Full-Stack Task Management System (Django 6)

A professional Full-Stack Task Management System built with **Django 6.0.3**, combining **server-side rendering (DTL)** and a **REST API (DRF)** with dynamic frontend interactions using **JavaScript**.

This project demonstrates real-world backend development skills, database design with MySQL, and interactive web UI development.

---

# 🔗 Links

- 📁 GitHub Repository: https://github.com/ibrahim-hamdouna/to-do-list
- 🌐 Live Demo: (https://justdo-97a6.onrender.com)

---

# 🏗 Architecture

This project follows a **hybrid Django architecture**:

* **DTL (Django Template Language):** Server-side rendered pages for tasks and UI
* **DRF (Django REST Framework):** REST API endpoints for data operations
* **JavaScript (Vanilla JS):** Dynamic UI actions (e.g. task actions without full reload)
* **HTML & CSS:** UI structure and styling

---

# 🛠 Tech Stack

* **Backend:** Django 6.0.3
* **API Layer:** Django REST Framework (DRF)
* **Database:** MySQL
* **Connector:** mysqlclient
* **Frontend:** HTML5, CSS3, JavaScript
* **Environment:** Python virtual environment (.venv)

---

# ✨ Core Features

* Create, update, and delete tasks (CRUD)
* Mark tasks as completed / pending
* Dynamic UI updates using JavaScript
* Server-rendered pages using Django Templates (DTL)
* REST API endpoints for task operations
* MySQL relational database integration
* Clean separation between backend logic and presentation layer

---

# 🔥 Key Highlights

* Hybrid architecture (DTL + API)
* Real-world Django project structure
* REST API built using DRF
* Interactive frontend using JavaScript
* Efficient database operations using Django ORM
* Clean and scalable code structure

---

# 📁 Project Structure

```text
to_do_list/
│
├── to_do_list/          # Project configuration (settings, urls)
│
├── todo_app/            # Main application
│   ├── models.py        # Database models (Task model)
│   ├── views.py         # Business logic (DTL + API logic)
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # Routing
│   ├── templates/       # Django templates (DTL)
│   └── static/          # CSS & JavaScript files
│
├── manage.py
└── requirements.txt
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/ibrahim-hamdouna/to-do-list.git
cd to-do-list
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Database (MySQL)

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 5. Run Migrations

```bash
python manage.py migrate
```

---

## 6. Start Server

```bash
python manage.py runserver
```

---

# 👨‍💻 Developer

**Ibrahim Hamdouna**
