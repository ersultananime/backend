# API тестирование

## Запуск сервера

```bash
cd src
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Сервер будет доступен на: http://localhost:8000

## API Endpoints

### 1. Главная страница
```
GET http://localhost:8000/
```

### 2. Получить всех пользователей
```
GET http://localhost:8000/users
```

**Ответ:**
```json
{
  "users": [
    {
      "id": 1,
      "full_name": "Айбек Серіков",
      "phone": "87071112233",
      "email": null,
      "address": "Абай көшесі, 10 үй"
    },
    {
      "id": 2,
      "full_name": "Динара Аманжол",
      "phone": "87015554433",
      "email": null,
      "address": "Достық даңғылы, 45 үй"
    }
  ]
}
```

### 3. Получить пользователя по ID
```
GET http://localhost:8000/users/1
```

### 4. Получить всех курьеров
```
GET http://localhost:8000/couriers
```

### 5. Получить все заказы
```
GET http://localhost:8000/orders
```

### 6. Получить заказ по ID
```
GET http://localhost:8000/orders/1
```

## Интерактивная документация API

FastAPI автоматически генерирует интерактивную документацию:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Вы можете тестировать API прямо из браузера!

## Пример запроса через curl

```bash
curl http://localhost:8000/users
curl http://localhost:8000/couriers
curl http://localhost:8000/orders
```

## Пример запроса через Python

```python
import requests

response = requests.get("http://localhost:8000/users")
print(response.json())
```

## Пример запроса через JavaScript/Fetch

```javascript
fetch('http://localhost:8000/users')
  .then(response => response.json())
  .then(data => console.log(data));
```
