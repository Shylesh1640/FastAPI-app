from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic import BaseModel, Field
from fastapi import status

app = FastAPI(title="My FastAPI Learning")

@app.get("/shy")
def root():
    return {"message": "Hello Shylesh!"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "type": str(type(user_id))}

@app.get("/search")
def search(q: str, page: int = 1, limit: int = 10):
    return {"query": q, "page": page, "limit": limit}

#curl comand = http://127.0.0.1:8000/search?q=fastapi&page=2&limit=5

class UserCreate(BaseModel):
    name: str
    email: str
    age: int | None = None
    
@app.post("/users")
def create_user(payload: UserCreate):
    return {"created": True, "user": payload.model_dump()}

#curl command = curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d "{\"name\": \"Shylesh\", \"email\": \"shylesh@example.com\", \"age\": 25}"


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    
@app.post("/products")
def create_product(p: ProductCreate):
    return p.model_dump()
#curl command = curl -X POST "http://127.0.0.1:8000/products" -H "Content-Type: application/json" -d "{\"name\": \"Product1\", \"price\": 100.0, \"stock\": 10}"

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"created": True}

#curl command = curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d "{}"

Fake_DB = {1: "Shylesh", 2: "John", 3: "Alice"}

@app.get("/users/db/{user_id}")
def user_from_db(user_id: int):
    if user_id not in Fake_DB:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "name": Fake_DB[user_id]}

#curl command = curl -X GET "http://127.0.0.1:8000/users/db/1"