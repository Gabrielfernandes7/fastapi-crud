from fastapi import APIRouter
from config.db import connection
from models.index import users

from schemas.index import User

user = APIRouter()

@user.get("/")
async def read_data():
    return connection.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
    return connection.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write_data(user: User):
    connection.execute(users.insert(),
        name = user.name,
        email = user.email,
        password = user.password)
    return connection.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_data(id: int, user: User):
    connection.execute(users.update(
        name = user.name,
        email = user.email,
        password = user.password
    )).where(users.c.id == id)
    return connection.execute(users.select()).fetchall()

@user.delete("/")
async def delete_data():
    connection.execute(users.delete().where(users.c.id == id))
    return connection.execute(users.select()).fetchall()
