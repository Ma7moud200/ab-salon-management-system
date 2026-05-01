# 💈 AB System (V1.0)

A full desktop management system for beauty salons, built using **Python (PySide6)** for the frontend and **FastAPI** for the backend.

---

## 📌 Overview

AB System is a desktop application designed to manage salon operations including:

* User authentication (Customer / Employee / Admin)
* Services management (Hair, Skin, Bride)
* Product inventory system
* Booking system
* REST API backend

The system uses **SQLite databases** and communicates between frontend and backend using HTTP requests.

---

## 🧠 Architecture

* **Frontend:** PySide6 (Desktop GUI) → 
* **Backend API:** FastAPI → 
* **Database:** SQLite (2 databases)

  * `Data.db` → main data
  * `WDB.db` → UI widgets data → 

---

## 🔐 Features

### 👤 Authentication System

* Multi-role login (Customer / Employee / Admin)
* Password hashing using `bcrypt`
* Admin-level permissions for editing and deleting

---

### 💇 Services Management

* Hair services
* Skin services
* Bride booking system
* Add / Edit / Delete services
* Order services directly from UI

---

### 🛒 Product Management

* Add new products
* Update price & quantity
* Sell / Use products
* Live search system
* Categorized products (Hair / Skin / Tint)

---

### 📅 Booking System

* Bride booking with:

  * Name
  * Phone
  * National ID
  * Price & Paid amount
  * Date
* Stored and retrieved from database

---

### 🌐 REST API (FastAPI)

Main endpoints include:

* `/login`
* `/signup`
* `/services/*`
* `/products/*`
* `/bride/book`

Example:

```bash
POST /login
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install requirements

```bash
pip install PySide6 fastapi uvicorn bcrypt requests
```

---

### 2️⃣ Run Backend

```bash
python api.py
```

Or using:

```bash
uvicorn api:app --reload
```

---

### 3️⃣ Initialize Database

```bash
python DATA.py
```

---

### 4️⃣ Run Application

```bash
python AB.py
```

---

## 📁 Project Structure

```
.
├── AB.py              # Main GUI application
├── api.py             # FastAPI backend
├── DATA.py            # Database initialization
├── server.py          # Run scripts automation → :contentReference[oaicite:3]{index=3}
├── Custom_Edits1.py   # Custom UI components → :contentReference[oaicite:4]{index=4}
├── shared.py          # Shared variables
├── view.png           # UI preview
├── Data.db            # Main database
├── WDB.db             # Widget database
```

---

## 🧩 Technologies Used

* Python
* PySide6 (Qt for Python)
* FastAPI
* SQLite
* bcrypt (password hashing)
* requests (API communication)

---

## 🚀 Future Improvements

* Add reporting system (analytics & charts)
* Improve UI/UX design
* Add role-based dashboards
* Docker support
* Cloud database integration

---

## 💡 Notes

* Backend must be running before launching the GUI
* The system is designed for local use (`127.0.0.1`)

---

## 👨‍💻 Author

Built as a learning project to explore:

* Full-stack Python development
* Desktop + API integration
* Real-world system design

---

⭐ If you like this project, consider giving it a star!
