# 🏥 AI Drug Analyzer

AI Drug Analyzer is a full-stack healthcare web application built using Flask and OpenFDA API.  
It allows users to securely register, log in, and search real drug information from the official FDA database.

---

## 🚀 Features

- 🔐 Secure User Registration & Login (JWT Authentication)
- 💊 Real Drug Information from OpenFDA API
- 📄 Automatic Drug Report File Generation
- 🗄 SQLite Database Integration
- 🌐 Frontend + Backend Architecture
- 🚀 Deployment Ready (Render)

---

## 🏗 Project Structure

```
ai-drug-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── utils/
│   │   ├── models.py
│   │   ├── config.py
│   │   ├── extensions.py
│   │   └── __init__.py
│   │
│   ├── run.py
│   ├── requirements.txt
│   └── reports/
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

### Backend
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLite
- OpenFDA API
- Gunicorn

### Frontend
- HTML
- JavaScript (Fetch API)

---

## 💊 Drug Information Source

This project uses the official OpenFDA API:

https://api.fda.gov/

Information fetched includes:
- Drug Description
- Usage / Indications
- Side Effects

---

## 🛠 How To Run Locally

### 1️⃣ Setup Backend

Open terminal:

```
cd backend
python -m venv venv
venv\Scripts\activate    (Windows)
pip install -r requirements.txt
python run.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

### 2️⃣ Run Frontend

Open new terminal:

```
cd frontend
python -m http.server 8000
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 🌍 Deployment (Render)

Backend:
- Root Directory → backend
- Build Command → pip install -r requirements.txt
- Start Command → gunicorn run:app

Frontend:
- Root Directory → frontend
- Publish Directory → .

---

## 📄 Auto Report Generation

Every drug search automatically creates a text report inside:

```
backend/reports/
```

---

## 👨‍💻 Author

Silar Mohammad Akmal  
B.Tech Engineering Student  
Healthcare SaaS Project

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub.