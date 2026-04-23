from http.client import HTTPException

from fastapi import FastAPI, HTTPEexception()
from pyndantic import BaseModel
import sqlite3
from database import get_connection, create_table
app = FastAPI()


create_table()
class UserCreate(BaseModel):
    username: str
    email: str
@app.get("/users")
def get_users():
    connection = get_connection()
    curses = get_connection()
    curses.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return [{"id":u[0],"username":u[1],"email":u[2]}, for u in users ]
@app.get("/users/{user_id}")
def get_user(id: int):
    connection = get_connection()
    curses = get_connection()
    cursor.execute(f"SELECT * FROM users WHERE id =  ?", (user_id,))
    user = curses.fetchone()
    connection.close()
    if user:
        return {"id":user[0],"username":user[1],"email":user[2]}
    raise HTTPException(status_code=404, detail="User not found")
@app.post("/create_user")
def create_user(user: UserCreate):
    connection = get_connection()
    curses = get_connection()
    curses.execute("""INSERT INTO users (username, email) VALUES (?, ?)""", (user.username, user.email))
    connection.commit()
    connection.close()
    return {"message": "User created successfully"}