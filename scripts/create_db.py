import sqlite3
import os

DB_PATH = "database.db"

def create_database():
    """Создаёт базу данных и инициализирует её"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Создание таблицы пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            email VARCHAR(100) UNIQUE,
            address TEXT
        )
    ''')
    
    # Создание таблицы курьеров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS couriers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            vehicle_type VARCHAR(50),
            is_available BOOLEAN DEFAULT 1
        )
    ''')
    
    # Создание таблицы заказов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(id),
            courier_id INTEGER REFERENCES couriers(id),
            pickup_address TEXT NOT NULL,
            delivery_address TEXT NOT NULL,
            price DECIMAL(10, 2),
            status VARCHAR(50) DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Вставка тестовых данных
    cursor.execute('''
        INSERT OR IGNORE INTO users (full_name, phone, address) VALUES 
        ('Айбек Серіков', '87071112233', 'Абай көшесі, 10 үй'),
        ('Динара Аманжол', '87015554433', 'Достық даңғылы, 45 үй')
    ''')
    
    cursor.execute('''
        INSERT OR IGNORE INTO couriers (full_name, vehicle_type) VALUES 
        ('Бақытжан', 'машина'),
        ('Руслан', 'велосипед')
    ''')
    
    cursor.execute('''
        INSERT OR IGNORE INTO orders (user_id, courier_id, delivery_address, price) VALUES 
        (1, 1, 'Төле би, 20 үй', 1500.00)
    ''')
    
    conn.commit()
    conn.close()
    
    print(f"✓ База данных успешно создана: {DB_PATH}")
    print("✓ Таблицы созданы: users, couriers, orders")
    print("✓ Тестовые данные добавлены")

if __name__ == "__main__":
    create_database()
