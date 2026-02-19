# FastAPI Learning App

A simple FastAPI application for learning API development with Python.

## Requirements

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn

## Installation

```bash
# Install dependencies using uv
uv sync

# Or using pip
pip install fastapi[standard] pydantic uvicorn
```

## Running the Application

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### Hello Endpoint
```
GET /shy
```
Returns a greeting message.

### Get User by ID
```
GET /user/{user_id}
```
Path parameter example with type conversion.

### Search
```
GET /search?q={query}&page={page}&limit={limit}
```
Query parameters example with defaults (page=1, limit=10).

**Example:**
```bash
curl "http://127.0.0.1:8000/search?q=fastapi&page=2&limit=5"
```

### Create User
```
POST /users
```
Request body validation with Pydantic.

**Example:**
```bash
curl -X POST "http://127.0.0.1:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"name": "Shylesh", "email": "shylesh@example.com", "age": 25}'
```

### Create Product
```
POST /products
```
Field validation with constraints (name: 2-50 chars, price > 0, stock >= 0).

**Example:**
```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name": "Product1", "price": 100.0, "stock": 10}'
```

### Create Item
```
POST /items
```
Returns 201 Created status code.

### Get User from Database
```
GET /users/db/{user_id}
```
Demonstrates HTTPException for error handling (returns 404 if user not found).

**Example:**
```bash
curl "http://127.0.0.1:8000/users/db/1"
```

## Interactive Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
