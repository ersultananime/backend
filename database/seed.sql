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
