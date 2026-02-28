import sqlite3
import os
from fastapi import FastAPI
from contextlib import closing

# Путь к базе данных
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.db")

app = FastAPI()

def get_db_connection():
    """Получить подключение к базе данных"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def read_root():
    return {"message": "Hello World! Сәлем, бұл біздің жеткізу қызметінің API-ы"}

@app.get("/users")
def get_users():
    """Получить всех пользователей"""
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = [dict(row) for row in cursor.fetchall()]
    return {"users": users}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Получить пользователя по ID"""
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
    return {"user": dict(user) if user else None}

@app.get("/couriers")
def get_couriers():
    """Получить всех курьеров"""
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM couriers")
        couriers = [dict(row) for row in cursor.fetchall()]
    return {"couriers": couriers}

@app.get("/orders")
def get_orders():
    """Получить все заказы"""
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = [dict(row) for row in cursor.fetchall()]
    return {"orders": orders}
