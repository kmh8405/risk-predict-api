# Risk Predict API

FastAPI 기반의 백엔드 서비스로, 사용자 인증 시스템과 리스크 예측 기능을 위한 구조를 구현한 프로젝트입니다.

---

## 🏗️ Architecture

- Framework: FastAPI
- Database: SQLite (async)
- ORM: SQLAlchemy (Async)
- Auth: Password Hashing (bcrypt), JWT (planned)

---

## 🚀 Features

### Day 1

- User signup API
- User login API (password verification)
- Async DB connection using SQLAlchemy
- Password hashing with bcrypt
- Modular project structure (auth / user / database)

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
├── user/
│   ├── models.py
│   ├── request.py
│   ├── response.py
│   ├── router.py
│
├── .gitignore
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

---

## 📌 Notes

* Async SQLAlchemy is used for non-blocking DB operations
* Passwords are securely stored using bcrypt hashing
* JWT authentication is planned for future implementation
* Project is designed with modular structure for scalability