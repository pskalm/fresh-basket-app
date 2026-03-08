# 🛒 FreshBasket — Online Grocery Delivery App

[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Built with](https://img.shields.io/badge/Built%20with-Flask-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Database](https://img.shields.io/badge/Database-MySQL-orange?style=for-the-badge&logo=mysql)](https://mysql.com)

---

## About the Project

FreshBasket is an online grocery shopping app where users can browse products, add them to a cart and place orders for home delivery. I built this because I wanted to get hands on with building something end to end — from the database all the way to the UI.

---

## What it can do

- Sign up and log in securely with hashed passwords
- Browse and search grocery products
- Add items to cart and remove them
- Place orders and see order confirmation
- Save and manage shipping addresses
- Admin can manage products, users and orders from a dashboard

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Python with Flask |
| Database | MySQL |
| Frontend | HTML, CSS, JavaScript |
| Auth | bcrypt password hashing |

---

## How to run it locally

Clone the repo:
```bash
git clone https://github.com/pskalm/freshbasket.git
cd freshbasket
```

Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:
```bash
pip install flask mysql-connector-python bcrypt python-dotenv requests
```

Set up the database:
```bash
mysql -u root -p freshbasket < fresh_basket.sql
```

Create a `.env` file inside the `web_dynamic` folder:
```
APP_SECRET_KEY=your_secret_key
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password
DB_DATABASE=freshbasket
```

Run the app:
```bash
cd web_dynamic
python app.py
```

Open 👉 `http://localhost:5000`

---

## Project Structure
```
FreshBasket/
├── web_dynamic/
│   ├── app.py           # all the routes and logic
│   ├── config.py        # database config
│   ├── templates/       # html pages
│   └── static/          # css, js, images
├── fresh_basket.sql     # database schema and data
└── requirements.txt
```

---

## Author

**Shubhangi Gupta**

📧 gshubhangi097@gmail.com | 🌐 [GitHub](https://github.com/pskalm)