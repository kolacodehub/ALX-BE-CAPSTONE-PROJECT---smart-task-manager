# Smart Task Manager API 🚀

A robust, secure RESTful API built with Django REST Framework, designed to help busy medical studnets students efficiently manage their daily tasks while staying motivated.

Developed as an ALX Backend Engineering Capstone project, this API goes beyond standard CRUD operations by integrating external motivation services and implementing advanced data retrieval techniques like pagination, search, and filtering—perfect for managing heavy workloads like juggling coding milestones with anatomy and biochemistry coursework.

## ✨ Features

- **Secure Authentication:** JSON Web Token (JWT) authentication ensures secure, stateless user sessions.
- **Data Isolation:** Users can strictly only create, view, update, and delete their own tasks.
- **Advanced Task Management:** \* Set task priorities (Low, Medium, High) and due dates.
  - Filter tasks by completion status or priority.
  - Search tasks by title or description.
  - Global pagination (10 items per page) for efficient data loading.
- **Daily Motivation Integration:** A custom endpoint fetches real-time inspirational quotes from the external ZenQuotes API, with built-in error handling and fallback mechanisms.

## 🛠️ Tech Stack

- **Backend:** Python 3, Django, Django REST Framework (DRF)
- **Authentication:** djanggorestframework-simplejwt (JWT)
- **Database:** SQLite (Development) / PostgreSQL (Later for Production)
- **External API:** Requests library fetching from ZenQuotes.io
- **Query Optimization:** django-filter

## 🚀 Local Setup & Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/yourusername/smart_task_manager.git
cd smart_task_manager
\`\`\`

### 2. Create and activate a virtual environment

\`\`\`bash

# Windows

python -m venv env
.\env\Scripts\activate

### 3. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Apply database migrations

\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

### 5. Create a superuser (for admin access)

\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 6. Run the development server

\`\`\`bash
python manage.py runserver
\`\`\`
The API will be available at `http://127.0.0.1:8000/`.

## 📡 API Endpoints Documentation

Include your JWT Access Token in the header for all protected routes:
`Authorization: Bearer <your_access_token>`

### Authentication

| Method | Endpoint                   | Description                                     | Access |
| :----- | :------------------------- | :---------------------------------------------- | :----- |
| POST   | `/api/auth/register/`      | Register a new user                             | Public |
| POST   | `/api/auth/login/`         | Login to receive JWT access/refresh tokens      | Public |
| POST   | `/api/auth/login/refresh/` | Obtain a new access token using a refresh token | Public |

### Tasks (Core Logic)

| Method    | Endpoint           | Description                           | Access    |
| :-------- | :----------------- | :------------------------------------ | :-------- |
| GET       | `/api/tasks/`      | List all tasks for the logged-in user | Protected |
| POST      | `/api/tasks/`      | Create a new task                     | Protected |
| GET       | `/api/tasks/<id>/` | Retrieve a specific task              | Protected |
| PUT/PATCH | `/api/tasks/<id>/` | Update a specific task                | Protected |
| DELETE    | `/api/tasks/<id>/` | Delete a specific task                | Protected |

### External Integration

| Method | Endpoint                 | Description                                        | Access    |
| :----- | :----------------------- | :------------------------------------------------- | :-------- |
| GET    | `/api/tasks/motivation/` | Fetches a daily inspirational quote from ZenQuotes | Protected |

## 🔍 Query Parameters (Filtering & Searching)

You can append query parameters to the `/api/tasks/` endpoint:

- **Filter by status:** `?is_completed=true` or `?is_completed=false`
- **Filter by priority:** `?priority=High`
- **Search:** `?search=keyword`
- **Order/Sort:** `?ordering=-due_date` (descending) or `?ordering=created_at` (ascending)

---

_Developed by Tiamiyu Abdulsalam Kolawole._
