-- Создание таблицы пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    address TEXT
);

-- Создание таблицы курьеров
CREATE TABLE couriers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    vehicle_type VARCHAR(50),
    is_available BOOLEAN DEFAULT TRUE
);

-- Создание таблицы заказов
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    courier_id INTEGER REFERENCES couriers(id),
    pickup_address TEXT NOT NULL,
    delivery_address TEXT NOT NULL,
    price DECIMAL(10, 2),
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Тесттік пайдаланушылар
INSERT INTO users (full_name, phone, address) VALUES 
('Айбек Серіков', '87071112233', 'Абай көшесі, 10 үй'),
('Динара Аманжол', '87015554433', 'Достық даңғылы, 45 үй');

-- Тесттік курьерлер
INSERT INTO couriers (full_name, vehicle_type) VALUES 
('Бақытжан', 'машина'),
('Руслан', 'велосипед');

-- Тесттік тапсырыс
INSERT INTO orders (user_id, courier_id, delivery_address, price) VALUES 
(1, 1, 'Төле би, 20 үй', 1500.00);
