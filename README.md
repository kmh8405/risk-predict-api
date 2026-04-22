# Risk Predict API

FastAPI 기반의 백엔드 서비스로, 사용자 인증 시스템과 리스크 예측 기능을 위한 구조를 구현한 프로젝트입니다.

---

## 🏗️ Architecture

- Framework: FastAPI
- Database: SQLite (async)
- ORM: SQLAlchemy (Async)
- Auth: Password Hashing (bcrypt), JWT (planned)
- External API: OpenAI (risk prediction)

---

## 🚀 Features

### Day 1

- User signup API
- User login API (password verification)
- Async DB connection using SQLAlchemy
- Password hashing with bcrypt
- Modular project structure (auth / user / database)

### Day 2

- JWT authentication (access token)
- Protected API using HTTPBearer
- Health profile creation API (1:1 with user)
- LLM-based risk prediction API (OpenAI)
- Prediction result storage in DB

---

## 📁 Project Structure

```
risk_predict/
├── auth/
│   ├── jwt.py
│   ├── password.py
│
├── database/
│   ├── connection.py
│   ├── orm.py
│
├── prediction/
│   ├── llm.py
│   ├── models.py
│   ├── router.py
│
├── user/
│   ├── models.py
│   ├── request.py
│   ├── response.py
│   ├── router.py
│
├── .gitignore
├── .env
├── .config.py
├── requirements.txt
├── README.md
├── main.py
├── db.sqlite
```

---

## 🛠️ How to Run

```bash
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

### Sign Up

POST /users

```json
{
  "email": "test@example.com",
  "password": "1234"
}
```

### Login

POST /users/login

```json
{
  "email": "test@example.com",
  "password": "1234"
}
```

Response:

```json
{
  "access_token": "..."
}
```

### Create Health Profile (Auth Required)

POST /health-profiles

Header:

```
Authorization: Bearer <access_token>
```

Body:

```
{
  "age": 25,
  "height_cm": 175,
  "weight_kg": 70,
  "smoking": false,
  "exercise_per_week": 3
}
```

### Risk Prediction (Auth Required)

POST /predictions

Header:

```
Authorization: Bearer <access_token>
```

---

## ⚠️ Troubleshooting

### 1. NameError: datetime not defined

**Error**

`NameError: name 'datetime' is not defined`

**Cause**

* `datetime`를 타입 힌트로 사용했지만 모듈로 import 되어 있었음

```python
import datetime ❌
```

→ 위 방식은 `datetime` 모듈 자체를 의미

**Solution**

```python
from datetime import datetime ✅
```

* `datetime` 클래스를 직접 import해야 타입 힌트로 사용 가능

### 2. ValueError: greenlet required

**Error**

```
ValueError: the greenlet library is required to use this function
No module named 'greenlet'
```

**Cause**

* Requires `greenlet` internally when running SQLAlchemy async
* No such package is installed

**Solution**

```bash
pip install greenlet
```

이후 다시 실행:

```python
import asyncio
from database.orm import init_db

asyncio.run(init_db())
```

### 3. SQLAlchemy: Table not created / Foreign key error

**Error (example)**

```
sqlalchemy.exc.NoReferencedTableError
```

**Cause**

- Models were not imported before running `create_all`
- SQLAlchemy only registers tables that are imported into metadata

**Wrong Example**

```python
from user.models import HealthProfile
from database.orm import init_db
import asyncio

asyncio.run(init_db())
```

→ Tables are not recognized because models are not loaded

**Solution**

```python
from user.models import User, HealthProfile
from prediction.models import HealthRiskPrediction
from database.orm import init_db
import asyncio

asyncio.run(init_db())
```

- Ensure all models are imported before DB initialization

---

## 📌 Notes

* Async SQLAlchemy is used for non-blocking DB operations
* JWT is used for stateless authentication
* Passwords are securely stored using bcrypt hashing
* Sensitive values are managed via `.env` and `config.py`
* Database tables can be initialized separately (no auto-create on startup)
* Designed with a modular structure for scalability
* Additional features (e.g., model improvements, validation) may be added in the future